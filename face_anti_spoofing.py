# import random
# import cv2
# import imutils
# import f_liveness_detection
# import questions
# import time
#
# # instantiate camera
# cv2.namedWindow('liveness_detection')
# cam = cv2.VideoCapture(0)
#
# # parameters
# COUNTER, TOTAL = 0,0
# counter_ok_questions = 0
# counter_ok_consecutives = 0
# limit_consecutives = 3
# limit_questions = 3
# counter_try = 0
# limit_try = 150
#
#
#
# def show_image(cam,text,color = (0,0,255)):
#     ret, im = cam.read()
#     im = imutils.resize(im, width=720)
#     #im = cv2.flip(im, 1)
#     cv2.putText(im,text,(10,50),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
#     return im
#
# start_time = time.time()
# for i_questions in range(0,limit_questions):
#     # generate random question
#     index_question = random.randint(0,3)
#     question = questions.question_bank(index_question)
#
#     # im = show_image(cam,question)
#     # cv2.imshow('liveness_detection',im)
#     # if cv2.waitKey(1) &0xFF == ord('q'):
#     #     break
#
#     for i_try in range(limit_try):
#         # <----------------------- receive data
#         ret, im = cam.read()
#         im = imutils.resize(im, width=720)
#         im = cv2.flip(im, 1)
#         # <----------------------- receive data
#         if i_try%5==0:
#             TOTAL_0 = TOTAL
#             out_model = f_liveness_detection.detect_liveness(im,question,COUNTER,TOTAL_0)
#             # TOTAL = out_model['total_blinks']
#             # COUNTER = out_model['count_blinks_consecutives']
#             # dif_blink = TOTAL-TOTAL_0
#             # if dif_blink > 0:
#             #     blinks_up = 1
#             # else:
#             #     blinks_up = 0
#
#             challenge_res = questions.challenge_result(question, out_model)
#
#             im = show_image(cam,question)
#             cv2.imshow('liveness_detection',im)
#             if cv2.waitKey(1) &0xFF == ord('q'):
#                 break
#
#             if challenge_res == "pass":
#                 im = show_image(cam,question+" : ok")
#                 cv2.imshow('liveness_detection',im)
#                 if cv2.waitKey(1) &0xFF == ord('q'):
#                     break
#
#                 counter_ok_consecutives += 1
#                 if counter_ok_consecutives == limit_consecutives:
#                     counter_ok_questions += 1
#                     counter_try = 0
#                     counter_ok_consecutives = 0
#                     break
#                 else:
#                     continue
#
#             elif challenge_res == "fail":
#                 counter_try += 1
#                 show_image(cam,question+" : fail")
#             # elif i_try == limit_try-1:
#             #     break
#
#
#     if counter_ok_questions ==  limit_questions:
#         while True:
#             im = show_image(cam,"LIFENESS SUCCESSFUL",color = (0,255,0))
#             cv2.imshow('liveness_detection',im)
#             if cv2.waitKey(1) &0xFF == ord('q'):
#                 break
#     elif i_try == limit_try-1:
#         while True:
#             im = show_image(cam,"LIFENESS FAIL")
#             cv2.imshow('liveness_detection',im)
#             if cv2.waitKey(1) &0xFF == ord('q'):
#                 break
#         break
#
#     else:
#         continue
# end_time = time.time()
# print(end_time - start_time)






# import cv2
# import f_liveness_detection
# import questions
# import imutils
# import time
#
# cv2.namedWindow('liveness_detection')
# cam = cv2.VideoCapture(0)
#
# COUNTER, TOTAL = 0, 0
# counter_ok_questions = 0
# counter_ok_consecutives = 0
# limit_consecutives = 3
# limit_questions = 2
# counter_try = 0
# limit_try = 250
# FRAME_MOD = 1
#
#
# def show_image(im, text, color=(0, 0, 255)):
#     # im = cv2.resize(im, (720, 560))
#     im = imutils.resize(im, width=720)
#     cv2.putText(im, text, (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
#     return im
#
#
# def get_frame(cam):
#     _, im = cam.read()
#     # im = cv2.resize(im, (720, 560))
#     im = imutils.resize(im, width=720)
#     im = cv2.flip(im, 1)
#     return im
#
#
# alive = False
# for i_questions in range(0, limit_questions):
#     question = questions.question_bank(i_questions)
#     text = question
#     for i_try in range(limit_try):
#         im = get_frame(cam)
#
#         if cv2.waitKey(1) &0xFF == ord('q'):
#             break
#
#         if i_try % FRAME_MOD == 0:
#             out_model = f_liveness_detection.detect_liveness(im, question, COUNTER, TOTAL)
#             challenge_res = questions.challenge_result(question, out_model)
#             if challenge_res == "pass":
#                 counter_ok_consecutives += 1
#                 if counter_ok_consecutives == limit_consecutives:
#                     counter_ok_questions += 1
#                     counter_try = 0
#                     counter_ok_consecutives = 0
#                     text = question + " : ok"
#                     break
#             # elif challenge_res == "fail":
#             #     counter_try += 1
#             #     text = question + " : fail"
#
#         im = show_image(im, text)
#         cv2.imshow('liveness_detection', im)
#
#     if counter_ok_questions == limit_questions:
#         alive = True
#         break
#
#
# im = get_frame(cam)
# if alive:
#     im = show_image(im, "LIFENESS SUCCESSFUL", color = (0, 255, 0))
# else:
#     im = show_image(im, "LIFENESS FAIL")
#
# while True:
#     cv2.imshow('liveness_detection', im)
#     if cv2.waitKey(1) &0xFF == ord('q'):
#         break


import cv2
import f_liveness_detection
import questions
import time

cv2.namedWindow('liveness_detection')
cam = cv2.VideoCapture(0)


COUNTER, TOTAL = 0, 0
counter_ok_questions = 0
counter_ok_consecutives = 0
limit_consecutives = 5
limit_questions = 3
counter_try = 0
limit_try = 250
FRAME_MOD = 1


def show_image(im, text, color=(0, 0, 255)):
    # im = cv2.resize(im, (1080, 860))
    cv2.putText(im, text, (50, 90), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
    return im


def get_frame(cam):
    _, im = cam.read()
    # im = cv2.resize(im, (1080, 860))
    im = cv2.flip(im, 1)
    return im


alive = False
for i_questions in range(0, limit_questions):
    question = questions.question_bank(i_questions)
    text = question
    for i_try in range(limit_try):
        im = get_frame(cam)

        if cv2.waitKey(1) &0xFF == ord('q'):
            break

        if i_try % FRAME_MOD == 0:
            out_model = f_liveness_detection.detect_liveness(im, question, COUNTER, TOTAL)
            challenge_res = questions.challenge_result(question, out_model)
            if challenge_res == "pass":
                counter_ok_consecutives += 1
                if counter_ok_consecutives == limit_consecutives:
                    counter_ok_questions += 1
                    counter_try = 0
                    counter_ok_consecutives = 0
                    text = question + " : ok"
                    break
            # elif challenge_res == "fail":
            #     counter_try += 1
            #     text = question + " : fail"

        im = show_image(im, text)
        # cv2.namedWindow('liveness_detection', cv2.WND_PROP_FULLSCREEN)
        # cv2.setWindowProperty('liveness_detection', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('liveness_detection', im)

    if counter_ok_questions == limit_questions:
        alive = True
        break




im = get_frame(cam)
if alive:
    im = show_image(im, "LIFENESS SUCCESSFUL", color = (0, 255, 0))
else:
    im = show_image(im, "LIFENESS FAIL")

while True:
    cv2.imshow('liveness_detection', im)
    if cv2.waitKey(1) &0xFF == ord('q'):
        break

