import re


def clean_training(annotated_trainings: str) -> list:
    """Takes the return from extract_dirty_trainings(files) removes tags and
    goal from training, creates bare utterances !!!problem with one extra
    space in front of some phrases!!!---> is really rare """
    ok_list = []
    no_annotation = re.sub(r'(\[(.*?)\])', '', annotated_trainings).lstrip()
    no_tags = no_annotation.replace('{', '')
    no_tags = no_tags.replace('}', '')
    no_tags = no_tags.replace('(', '')
    no_tags = no_tags.replace(')', '')
    no_tags = no_tags.replace('"', "")
    no_tags = no_tags.replace('utterance  ', '')
    no_tags = no_tags.replace('utterance ', '')
    list_empty_spaces = [no_tags]
    for i in list_empty_spaces:
        separate_i = i.split("\n")
        for utt in separate_i:
            if utt != "":
                no_white_spaces = " ".join(utt.split())
                ok_list.append(no_white_spaces)
    return ok_list
