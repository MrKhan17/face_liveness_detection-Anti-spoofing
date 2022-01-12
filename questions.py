def question_bank(index):
    questions = [
                "smile",
                "blink eyes",
                "turn face right",
                "turn face left"]
    return questions[index]

def challenge_result(question, out_model):
    print((out_model))
    if question == "smile":
        if len(out_model["emotion"]) == 0:
            challenge = "fail"
        elif out_model["emotion"][0] == "happy": 
            challenge = "pass"
        else:
            challenge = "fail"

    elif question == "turn face right":
        if len(out_model["orientation"]) == 0:
            challenge = "fail"
        elif out_model["orientation"][0] == "right":
            challenge = "pass"
        else:
            challenge = "fail"

    elif question == "turn face left":
        if len(out_model["orientation"]) == 0:
            challenge = "fail"
        elif out_model["orientation"][0] == "left":
            challenge = "pass"
        else:
            challenge = "fail"

    elif question == "blink eyes":
        if out_model['blinks_up'] == 1:
            challenge = "pass"
        else:
            challenge = "fail"

    # elif question == "surprise":
    #     if len(out_model["emotion"]) == 0:
    #         challenge = "fail"
    #     elif out_model["emotion"][0] == "surprise":
    #         challenge = "pass"
    #     else:
    #         challenge = "fail"
    #
    # elif question == "angry":
    #     if len(out_model["emotion"]) == 0:
    #         challenge = "fail"
    #     elif out_model["emotion"][0] == "angry":
    #         challenge = "pass"
    #     else:
    #         challenge = "fail"

    return challenge