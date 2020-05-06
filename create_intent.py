import dialogflow_v2 as dialogflow
import argparse
import json
PROJECT_ID = os.environ['PROJECT_ID']


def get_file_with_training_phrases():
    parser = argparse.ArgumentParser()
    parser.add_argument('training_phrases', help='Training phrases')
    return parser.parse_args().training_phrases


def create_intent(project_id, display_name, training_phrases_parts,
                  message_texts):
    intents_client = dialogflow.IntentsClient()
    parent = intents_client.project_agent_path(project_id)
    reply_response = []
    reply_response.append(message_texts)
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


def main():
    training_phrases = get_file_with_training_phrases()
    with open(training_phrases, "r") as phrases:
        file_contents = json.load(phrases)
        for display_name, dialog in file_contents.items():
            create_intent(PROJECT_ID, display_name, dialog['questions'], dialog['answer'])


if __name__ == '__main__':
    main()
