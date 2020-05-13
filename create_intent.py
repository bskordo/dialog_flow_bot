import dialogflow_v2 as dialogflow
import argparse
import json



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('training_phrases', help='Training phrases')
    return parser.parse_args()


def create_intent(project_id, display_name, training_phrases_parts,
                  message_text):
    intents_client = dialogflow.IntentsClient()
    parent = intents_client.project_agent_path(project_id)
    reply_response =[message_text]
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.types.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)
    text = dialogflow.types.Intent.Message.Text(text=reply_response)
    message = dialogflow.types.Intent.Message(text=text)
    intent = dialogflow.types.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message])
    response = intents_client.create_intent(parent, intent)


def load_json_phrases(training_phrases):
    with open(training_phrases, "r") as phrases:
        return json.load(phrases)



def main():
    project_id = os.environ['project_id']
    phrases = parse_args()
    training_phrases = phrases.training_phrases
    file_subjects = load_json_phrases(training_phrases)
        for display_name, dialog in file_subjects.items():
            create_intent(project_id, display_name, dialog['questions'], dialog['answer'])


if __name__ == '__main__':
    main()
