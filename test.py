from src.promptml.parser import PromptParser

promptml_code = '''
@vars
    conditionVar = "true"
    NextVar = "ABC"
@end

@prompt
    @title
        "Conditional Prompt Example"
    @end
    @context 
        This is a sampl context.
    @end
    @objective 
        Achieve this objective based on the condition.
    @end

    @if conditionVar == "true" {
        @objective 
            Achieve this objective based on the condition.
        @end
    }
    @else {
        "This is a sample context."
    }
@end
'''
parser = PromptParser(promptml_code, user_input={"EDUCATION_LEVEL": "high school"})
prompt = parser.parse()

print(prompt)