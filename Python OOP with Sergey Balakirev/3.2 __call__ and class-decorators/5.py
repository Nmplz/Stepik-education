class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list

    def __call__(self, str_list):

        if not self.type_list in ["ol", "ul"]:
            self.type_list = "ul"

        result = f"<{self.type_list}>"
        for i in str_list:
            result += f"\n<li>{i}</li>"
        result += f"\n</{self.type_list}>"
        return result
