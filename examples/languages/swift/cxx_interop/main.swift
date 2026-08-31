import CxxStdlib
import LunaSVGMod

// lunasvg has no styling of its own; this stylesheet colors the markup below.
let svg = """
<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300">
  <rect class="sky" x="0" y="0" width="400" height="230"/>
  <polygon class="hills" points="0,230 90,140 170,230 240,160 330,230 400,180 400,230"/>
  <rect class="ground" x="0" y="215" width="400" height="85"/>
  <g class="cloud" transform="translate(70,55)">
    <ellipse cx="0" cy="0" rx="26" ry="14"/>
    <ellipse cx="20" cy="-6" rx="20" ry="12"/>
    <ellipse cx="-20" cy="4" rx="18" ry="10"/>
  </g>
  <text class="title" x="200" y="40" text-anchor="middle" font-size="22">Swift's C++ Interoperability</text>
  <g class="cloud" transform="translate(230,85)">
    <ellipse cx="0" cy="0" rx="22" ry="12"/>
    <ellipse cx="18" cy="-4" rx="16" ry="10"/>
    <ellipse cx="-16" cy="3" rx="15" ry="9"/>
  </g>
</svg>
"""

let css = ".sky{fill:#8ECBEB} .hills{fill:#8FA89B} .ground{fill:#8FC77E} .cloud{fill:#FFFFFF} .title{fill:#3B4A40}"

let document = lunasvg.Document.loadFromData(std.string(svg))
document.pointee.applyStyleSheet(std.string(css))

let bitmap = document.pointee.renderToBitmap()
_ = bitmap.writeToPng(std.string("summer.png"))

print("Generated summer.png")
