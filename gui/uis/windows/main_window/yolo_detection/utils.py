# yolo_detection/utils.py

import json

def load_detected_objects(file_path="detected_objects.json"):
    with open(file_path, "r") as f:
        detected_objects = json.load(f)
    return detected_objects

def print_detected_objects(detected_objects):
    if not detected_objects['detected_objects']:  # 리스트가 비어있는 경우
        return "🔍 검출된 대상 없음"

    if 'detected_objects' in detected_objects:
        text = "🔽 검출된 객체 정보 🔽\n\n"
        for obj in detected_objects['detected_objects']:
            text += (
                f"📍 대상: {obj['class_name']}"
                f" index: {obj['index']}\n"
                f" X: {obj['X']}, Y: {obj['Y']}, Z: {obj['Z']}\n\n"
            )
        return text  # 문자열 반환
    else:
        return "⚠️ 오류: detected_objects 키가 없습니다."
