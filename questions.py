def question_bank(index):
    questions = [
                # "smile",
                # "blink eyes",
                "turn face left",
                "turn face right",
                "look front"]
    return questions[index]

def challenge_result(question, out_model):
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
        if out_model['count_blinks_consecutives'] == 1:
            challenge = "pass"
        else:
            challenge = "fail"

    elif question == "look front":
        if len(out_model["orientation"]) == 0:
            challenge = "fail"
        elif out_model["orientation"][0] == "frontal":
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