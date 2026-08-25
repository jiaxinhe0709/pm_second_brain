import AppKit
import Foundation
import PDFKit

guard CommandLine.arguments.count == 3 else {
    fputs("usage: render_pdf <input.pdf> <output-prefix>\n", stderr)
    exit(2)
}

let inputPath = CommandLine.arguments[1]
let outputPrefix = CommandLine.arguments[2]

guard let document = PDFDocument(url: URL(fileURLWithPath: inputPath)) else {
    fputs("cannot open \(inputPath)\n", stderr)
    exit(1)
}

var extracted = ""
for index in 0..<document.pageCount {
    guard let page = document.page(at: index) else { continue }
    extracted += "\n\n===== PAGE \(index + 1) =====\n\n"
    extracted += page.string ?? ""

    let bounds = page.bounds(for: .mediaBox)
    let targetWidth: CGFloat = 1600
    let targetHeight = targetWidth * bounds.height / bounds.width
    let image = page.thumbnail(of: NSSize(width: targetWidth, height: targetHeight), for: .mediaBox)
    guard let tiff = image.tiffRepresentation,
          let bitmap = NSBitmapImageRep(data: tiff),
          let png = bitmap.representation(using: .png, properties: [:]) else {
        fputs("cannot render page \(index + 1)\n", stderr)
        exit(1)
    }
    let pagePath = String(format: "%@-%03d.png", outputPrefix, index + 1)
    try png.write(to: URL(fileURLWithPath: pagePath))
}

try extracted.write(toFile: outputPrefix + ".txt", atomically: true, encoding: .utf8)
print("pages=\(document.pageCount) prefix=\(outputPrefix)")
