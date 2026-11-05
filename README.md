# clutter-vlm

ATML project, study 3: does visual clutter make a VLM worse at counting shapes and following lines, and does clutter the model can name hurt more than clutter it can't name?

The datasets are the four Shapes/Objects/Lines VQA sets in the `atml-shapes-vqa` Hugging Face organisation. The predictions and methods are fixed in `docs/study3_methodology.pdf` before any model runs.

## Running on Kaggle

GPU T4, internet on, secret `HF_TOKEN` (a read token of an account in the `atml-shapes-vqa` organisation). One notebook cell:

```
!git clone -q https://github.com/zoyakhan51/clutter-vlm /tmp/code && cd /tmp/code && git checkout -q COMMIT
import os; from kaggle_secrets import UserSecretsClient; os.environ["HF_TOKEN"] = UserSecretsClient().get_secret("HF_TOKEN")
!cd /tmp/code && python run_predictions.py --model qwen3vl4b --split all
!cd /tmp/code && python run_nameability.py --model qwen3vl4b
!cd /tmp/code && python analysis.py --model qwen3vl4b
```

Replace `COMMIT` with the commit being run. Add `--per-version 20` to the first two scripts for a trial run.

- `run_predictions.py` answers every image of the four datasets and runs each dataset's official `vqa_scoring.py`. The model's reply is started with the first words of each answer format (`circle:`, `apple:`, `box:`), so it answers instead of explaining.
- `run_nameability.py` cuts every squiggle and every `other_shapes` shape of Shapes Hard out of its image and records what the model calls it (H2 nameability score, Stage 0 naming check).
- `analysis.py` computes every H1-H8 result with 95% bootstrap intervals over scenes, exactly as fixed in `docs/study3_methodology.pdf`.

Outputs: `/kaggle/working/preds` (answers, scorer output, nameability answers, `environment_<model>.json`) and `/kaggle/working/results` (`results_<model>.json` and a plain-text `summary_<model>.txt`).
