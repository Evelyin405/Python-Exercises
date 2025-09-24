Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> play_list = ["Track A","Track B","Track C","Track D"]
>>> play_list.remove("Track C")
>>> play_list.insert(0,"Track X")
>>> play_list.remove("Track D")
>>> play_list.insert(1,"Track D")
>>> print(" ".join(play_list))
Track X Track D Track A Track B

