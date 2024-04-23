import os
import json

def convert_json_files(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            with open(os.path.join(input_folder, filename), 'r') as f:
                data = json.load(f)
                clips = data['Data'][0]['Clips']

                converted_clips = []
                for clip in clips:
                    video_id = f"{data['Data'][0]['Video_title']} clip {clip['clip_id']}"
                    qa_pair = {
                        "q": "What's the content of this video?",
                        "a": clip["Transcript"],
                        "video_id": video_id
                    }
                    converted_clips.append(qa_pair)

                output_data = json.dumps(converted_clips, indent=4)
                output_filename = f"{data['Data'][0]['Video_title']}_converted.json"
                with open(os.path.join(output_folder, output_filename), 'w') as out_file:
                    out_file.write(output_data)

input_folder = 'json_data'
output_folder = 'json_new'
convert_json_files(input_folder, output_folder)
