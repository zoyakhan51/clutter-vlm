# the vlms the study can run, pinned so every run uses exactly the same weights
# a revision of None means the newest weights are used and their exact revision is printed and saved,
# so it can be pinned here after the trial run
MODELS = {
    "qwen3vl2b":("Qwen/Qwen3-VL-2B-Instruct","89644892e4d85e24eaac8bacfd4f463576704203"),
    "qwen3vl4b":("Qwen/Qwen3-VL-4B-Instruct","ebb281ec70b05090aa6165b016eac8ec08e71b17"),
    "gemma4e4b":("google/gemma-4-E4B-it",None),
    "internvl35_4b":("OpenGVLab/InternVL3_5-4B-HF",None),
    "molmo2_4b":("allenai/Molmo2-4B",None),
    "qwen3vl8b":("Qwen/Qwen3-VL-8B-Instruct",None),
}
