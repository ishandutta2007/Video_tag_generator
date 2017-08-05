# Video_tag_generator
This is a small script that takes any video files and try to generate appropriate tags associated with the video.
The tags are only printed if they are present in the `db.txt` (Here dbpedia ontology classes and subclasses).
The script uses speech recognition engine `sphinx` and generate simple tags based on `nltk`, `tokenizer`, and `lemmatizer`.
This script do no model creation and training (kept for later). The script leaves the audio file in `.wav` format that is used
by `sphinx`

### Todo:
- [ ] Create more sphositicated text processing and train models to chose best tags from the keywords.
- [ ] Optimize the code wrt time
- [ ] Get collaborator

### Files:
`db.txt`: Contains the list of dbpedia-ontology classes and subclasses

`tag_single_thread.py`: Script to genrerate the tags on console. The input parameter from cmd line is `regex` mathing all the
video files in the directory one wish to process

`tag_multi_thread.py`: Multithreaded version of the `tag_single_thread.py` script. (oviosly :p)

### Main Dependencies:
- `py3`
- `spechrecognition`
- `pocketsphinx`
- `nltk`

### Example Run:
Clone this repo and run this:

`python3 tag_single_thread.py 'Kunal*.mkv'`

or 

`python3 tag_multi_thread.py 'Kunal*.mkv'`

This code runs the script on all files matching the regex `Kunal*.mkv`

I know videos should not be added to git repo. But still (:p) adding it for you to test.
