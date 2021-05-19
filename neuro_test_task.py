

def greet(prompt_name='hello', stop_call=False):
    if prompt_name == 'hello':
        nv.say(prompt_name,  nn.env('name'))
    else:
        nv.say(prompt_name)

    with nv.listen(
            ('confirm', 'wrong_time', 'repeat', 500, 'OR'),
            entities=['confirm', 'wrong_time', 'repeat']) as result:

        if result.has_entities():

            if result.has_entity('repeat'):
                greet('hello_repeat')

            elif result.has_entity('wrong_time'):
                hangup('hangup_wrong_time')

            elif result.entity('confirm'):
                main('recommend_main')

            else:
                hangup('hangup_wrong_time')

        elif result.utterance():
            main('recommend_main')

        else:

            if stop_call:
                hangup('hangup_null')
            else:
                greet('hello_null', stop_call=True)


def main(prompt_name, stop_call=False):
    nv.say(prompt_name)
    with nv.listen(
            ('recommendation_score', 'wrong_time', 'repeat', 'recommendation', 'question', 4000, 'OR'),
            entities=['recommendation_score', 'wrong_time', 'repeat', 'recommendation', 'question']) as result:

        if result.has_entities():

            if result.has_entity('recommendation_score'):

                if 0 <= result.entity('recommendation_score') <= 8:
                    hangup('hangup_negative')
                else:
                    hangup('hangup_positive')

            elif result.has_entity('wrong_time'):
                hangup('hangup_wrong_time')

            elif result.has_entity('repeat'):
                main('recommend_repeat')

            elif result.has_entity('recommendation'):

                if result.entity('recommendation') == 'negative':
                    main('recommend_score_negative')

                elif result.entity('recommendation') == 'positive':
                    main('recommend_score_positive')

                elif result.entity('recommendation') == 'neutral':
                    main('recommend_score_neutral')

                else:
                    main('recommend_repeat_2')

            else:
                nv.say('forward')
                bridge_action()

        elif result.utterance():

            if stop_call:
                hangup('hangup_null')
            else:
                main('recommend_default', stop_call=True)

        else:

            if stop_call:
                hangup('hangup_null')
            else:
                main('recommend_null', stop_call=True)


def hangup(prompt_name):
    nv.say(prompt_name)
    nn.dialog.result = nn.RESULT_DONE
    hangup_action()


if __name__ == '__main__':

    params_for_nn_call = {
        'msisdn': '+70000000000'  # etc.
    }

    nn.call(**params_for_nn_call, script=greet)





