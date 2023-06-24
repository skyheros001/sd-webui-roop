import tempfile
from ifnude import detect
#导入logger模块
from scripts.roop_logging import logger

def convert_to_sd(img):
    shapes = []
    chunks = detect(img)
    for chunk in chunks:
        scores = chunk["score"]
        logger.info(f"当前图片评分为 {scores}")
        #原来内容是 > 0.7，即高于0.7即为nsfw，压入内容，则any(shapes)=true后默认不换脸
        #不建议删除评分检测，保留detect，可以自由切换使用场景
        shapes.append(chunk["score"] < -9999)
    return [any(shapes), tempfile.NamedTemporaryFile(delete=False, suffix=".png")]
