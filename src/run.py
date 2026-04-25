import math

def generate_polygon_svg(n, radius=200, center=(250, 250), filename="logo.svg"):
    cx, cy = center
    
    # 计算顶点
    points = []
    for i in range(n):
        angle = 2 * math.pi * i / n - math.pi / 2  # 从正上方开始
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        points.append((x, y))

    # 开始写 SVG
    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="500" height="500">')

    # 画所有连接线（包括对角线和边）
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            svg_lines.append(
                f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                f'stroke="black" stroke-width="1"/>'
            )

    # 画顶点
    for x, y in points:
        svg_lines.append(
            f'<circle cx="{x}" cy="{y}" r="3" fill="black"/>'
        )

    svg_lines.append('</svg>')

    # 写入文件
    with open(filename, "w") as f:
        f.write("\n".join(svg_lines))

    print(f"SVG 已生成: {filename}")


generate_polygon_svg(16)
