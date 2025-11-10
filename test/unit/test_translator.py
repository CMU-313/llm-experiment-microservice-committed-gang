from src.translator import translate_content
import src.translator as translator


def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message"

def test_llm_normal_response():
    is_english, translated_content = translate_content("This should not be translated")
    assert is_english == True
    assert translated_content == "This should not be translated"

    is_english, translated_content = translate_content("Hola")
    assert is_english == False
    assert translated_content == "Hello"

def test_llm_gibberish_response():
    is_english, translated_content = translate_content("asp12345difjasdf")
    assert is_english == False
    assert translated_content == "asp12345difjasdf"