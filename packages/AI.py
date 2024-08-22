import google.generativeai as genai

class Model:
    def __init__(self):
        """
        모델을 불러오고 설정을 초기화

        temperature, top_p, top_k: 생성할 답변의 다양성 조절 (낮을수록 정확하고 일관적, 높을수록 다양하고 창의적)
        max_output_tokens: 생성할 답변의 최대 길이
        """

        generation_config = {
            'temperature': 0.9,
            'top_p': 1,
            'top_k': 1,
            'max_output_tokens': 2048
        }
        self.model = genai.GenerativeModel('gemini-1.5-flash-latest',
                                           generation_config=generation_config)

    def __call__(self, prompt):
        """
        클래스 인스턴스를 함수처럼 직접 호출할 때 호출되는 함수

        ex)
        model = Model()
        response = model("hi")
        """

        response = self.model.generate_content(prompt) # 실제로 모델에 리퀘스트를 보내는 부분
        
        return response.text


if __name__ == "__main__": # 테스트용 코드 (파일을 import해서 사용할 때는 실행되지 않음)
    with open("../API_KEY.txt", "r") as f:
        API_KEY = f.read().strip()

    genai.configure(api_key=API_KEY)

    model = Model()
    print(model("hi"))
