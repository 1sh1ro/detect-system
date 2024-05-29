# 1.py
# This is the main processing file for the application.
# It takes an image as input and outputs text.
# You can add your image processing and text extraction code here.

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import webcolors
import webbrowser
import sys

standard_colors = [
    {'item': '尿胆原', 'time': '60秒', 'value': '3.3', 'color': '#fdeabf'},
    {'item': '尿胆原', 'time': '60秒', 'value': '16', 'color': '#f3b18f'},
    {'item': '尿胆原', 'time': '60秒', 'value': '33', 'color': '#f19b76'},
    {'item': '尿胆原', 'time': '60秒', 'value': '66', 'color': '#ee856f'},
    {'item': '尿胆原', 'time': '60秒', 'value': '131', 'color': '#e56c67'},
    
    {'item': '胆红素', 'time': '60秒', 'value': '阴性', 'color': '#fffbef'},
    {'item': '胆红素', 'time': '60秒', 'value': '17', 'color': '#f6e3b9'},
    {'item': '胆红素', 'time': '60秒', 'value': '50', 'color': '#e0cbad'},
    {'item': '胆红素', 'time': '60秒', 'value': '100', 'color': '#e8c8b4'},

    {'item': '酮体', 'time': '60秒', 'value': '阴性', 'color': '#f9c49b'},
    {'item': '酮体', 'time': '60秒', 'value': '0.5', 'color': '#f2b191'},
    {'item': '酮体', 'time': '60秒', 'value': '1.5', 'color': '#f1848d'},
    {'item': '酮体', 'time': '60秒', 'value': '4.0', 'color': '#c9536d'},
    {'item': '酮体', 'time': '60秒', 'value': '8.0', 'color': '#9c325c'},

    {'item': '肌酐', 'time': '60秒', 'value': '0.9', 'color': '#f0eade'},
    {'item': '肌酐', 'time': '60秒', 'value': '4.4', 'color': '#ece6d8'},
    {'item': '肌酐', 'time': '60秒', 'value': '8.8', 'color': '#ecddd6'},
    {'item': '肌酐', 'time': '60秒', 'value': '17.7', 'color': '#d9c7cb'},
    {'item': '肌酐', 'time': '60秒', 'value': '26.5', 'color': '#c5aebe'},

    {'item': '血', 'time': '60秒', 'value': '阴性', 'color': '#f9bf1d'},
    {'item': '血', 'time': '60秒', 'value': 'ban10', 'color': '#ffc01f'},
    {'item': '血', 'time': '60秒', 'value': '10', 'color': '#d3b426'},
    {'item': '血', 'time': '60秒', 'value': '25', 'color': '#aca53b'},
    {'item': '血', 'time': '60秒', 'value': '80', 'color': '#689145'},
    {'item': '血', 'time': '60秒', 'value': '200', 'color': '#136c3a'},

    {'item': '蛋白质', 'time': '60秒', 'value': '阴性', 'color': '#ebef9a'},
    {'item': '蛋白质', 'time': '60秒', 'value': '0.2', 'color': '#d8e699'},
    {'item': '蛋白质', 'time': '60秒', 'value': '0.3', 'color': '#bfd597'},
    {'item': '蛋白质', 'time': '60秒', 'value': '1.0', 'color': '#96ccaa'},
    {'item': '蛋白质', 'time': '60秒', 'value': '3.0', 'color': '#85c5ba'},

    {'item': '微白蛋白', 'time': '60秒', 'value': '阴性', 'color': '#f5f8d9'},
    {'item': '微白蛋白', 'time': '60秒', 'value': '0.15', 'color': '#bde1d7'},

    {'item': '亚硝酸盐', 'time': '60秒', 'value': '阴性', 'color': '#feede3'},
    {'item': '亚硝酸盐', 'time': '60秒', 'value': '阳性', 'color': '#fffdee'},

    {'item': '白细胞', 'time': '60秒', 'value': '阴性', 'color': '#fcfac9'},
    {'item': '白细胞', 'time': '60秒', 'value': '15', 'color': '#ebe0ce'},
    {'item': '白细胞', 'time': '60秒', 'value': '70', 'color': '#d8d0bf'},
    {'item': '白细胞', 'time': '60秒', 'value': '125', 'color': '#bb8ca4'},
    {'item': '白细胞', 'time': '60秒', 'value': '500', 'color': '#7e557d'},

    {'item': '葡萄糖', 'time': '60秒', 'value': '阴性', 'color': '#9accc9'},
    {'item': '葡萄糖', 'time': '60秒', 'value': '5.5', 'color': '#a7d394'},
    {'item': '葡萄糖', 'time': '60秒', 'value': '14', 'color': '#9ab231'},
    {'item': '葡萄糖', 'time': '60秒', 'value': '28', 'color': '#a98d06'},
    {'item': '葡萄糖', 'time': '60秒', 'value': '55', 'color': '#9a7830'},

    {'item': '比重', 'time': '60秒', 'value': '1.000', 'color': '#3c7139'},
    {'item': '比重', 'time': '60秒', 'value': '1.005 正常', 'color': '#7b8830'},
    {'item': '比重', 'time': '60秒', 'value': '1.010', 'color': '#aaa418'},
    {'item': '比重', 'time': '60秒', 'value': '1.015', 'color': '#c2ab0f'},
    {'item': '比重', 'time': '60秒', 'value': '1.020', 'color': '#ccae02'},
    {'item': '比重', 'time': '60秒', 'value': '1.025', 'color': '#d9af2e'},
    {'item': '比重', 'time': '60秒', 'value': '1.030', 'color': '#e7ba1f'},

    {'item': '酸碱度', 'time': '60秒', 'value': '5', 'color': '#f2cc02'},
    {'item': '酸碱度', 'time': '60秒', 'value': '6', 'color': '#bcb80c'},
    {'item': '酸碱度', 'time': '60秒', 'value': '7', 'color': '#889a2d'},
    {'item': '酸碱度', 'time': '60秒', 'value': '8', 'color': '#4c7d34'},
    {'item': '酸碱度', 'time': '60秒', 'value': '9', 'color': '#01508b'},

    {'item': 'VC', 'time': '60秒', 'value': '0', 'color': '#00618b'},
    {'item': 'VC', 'time': '60秒', 'value': '0.5', 'color': '#5eb0ae'},
    {'item': 'VC', 'time': '60秒', 'value': '1.5', 'color': '#a7c5b1'},
    {'item': 'VC', 'time': '60秒', 'value': '3.0', 'color': '#e4e3a4'},
    {'item': 'VC', 'time': '60秒', 'value': '6.0', 'color': '#efeb9b'},

    {'item': '钙离子', 'time': '60秒', 'value': '<=1.0', 'color': '#fef6f3'},
    {'item': '钙离子', 'time': '60秒', 'value': '2.5', 'color': '#f7ebeb'},
    {'item': '钙离子', 'time': '60秒', 'value': '5.0', 'color': '#f0d9e1'},
    {'item': '钙离子', 'time': '60秒', 'value': '7.5', 'color': '#e6bfd3'},
    {'item': '钙离子', 'time': '60秒', 'value': '>=10', 'color': '#c7a4c4'},
]

def detect_and_draw_color_blocks(image_path):
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or unable to open.")
    
    # 获取图像的高度和宽度
    height, width, _ = image.shape
    
    # 计算两条水平线的位置
    line1_y = height // 3
    line2_y = 2 * height // 3
    
    # 计算七条垂直线的位置
    vertical_lines_x = [(i * width) // 8 for i in range(1, 8)]
    
    # 用于存储交点的颜色值
    color_blocks = []
    
    # 在图像上画线并获取交点的颜色
    for x in vertical_lines_x:
        for y in [line1_y, line2_y]:
            # 获取交点的颜色
            color = image[y, x]
            # 转换为十六进制的RGB颜色值
            hex_color = '#{:02x}{:02x}{:02x}'.format(color[2], color[1], color[0])
            color_blocks.append(hex_color)
            # 在图像上画交点
            cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
    
    # 在图像上画水平线
    cv2.line(image, (0, line1_y), (width, line1_y), (255, 0, 0), 2)
    cv2.line(image, (0, line2_y), (width, line2_y), (255, 0, 0), 2)
    
    # 在图像上画垂直线
    for x in vertical_lines_x:
        cv2.line(image, (x, 0), (x, height), (255, 0, 0), 2)

    item=['尿胆原', '胆红素', '酮体', '肌酐',  '血', '蛋白质', '微白蛋白', '亚硝酸盐', '白细胞','葡萄糖', '比重',  '酸碱度', 'VC','钙离子']
    
    item_color_mapping = {item: color for item, color in zip(item, color_blocks)}

    matched_results = match_color_to_standard(item_color_mapping, standard_colors)
    return [{'item': result['item'], 'value': result['value']} for result in matched_results]
    # return(matched_results)
    #for result in matched_results:
    #    print({'item': result['item'], 'value': result['value']})

def color_similarity(color1, color2):
        return np.sqrt(sum((component1 - component2)**2 for component1, component2 in zip(color1, color2)))

def match_color_to_standard(item_color_mapping, standard_colors):
    matched_results = []

    for item, color_hex in item_color_mapping.items():
        input_color = webcolors.hex_to_rgb(color_hex)
        closest_match = None
        min_difference = float('inf')
        
        for entry in standard_colors:
            if entry['item'] == item:
                standard_color = webcolors.hex_to_rgb(entry['color'])
                difference = color_similarity(input_color, standard_color)
                
                if difference < min_difference:
                    min_difference = difference
                    closest_match = entry
        
        if closest_match:
            matched_results.append({
                'item': item,
                'input_color': color_hex,
                'closest_standard_color': closest_match['color'],
                'time': closest_match['time'],
                'value': closest_match['value']
            })
    
    return matched_results

# 使用示例
# detect_and_draw_color_blocks('2.png')


if __name__ == "__main__":
    # 检查是否有足够的命令行参数
    if len(sys.argv) < 2:
        print("Usage: python 1.py <image_path>")
        sys.exit(1)  # 退出程序，因为没有提供必要的参数

    image_path = sys.argv[1]  # 获取命令行提供的第二个参数（索引1）
    result = detect_and_draw_color_blocks(image_path)
    print(result)
