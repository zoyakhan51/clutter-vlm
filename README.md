# clutter-vlm

ATML project, study 3: does visual clutter make a VLM worse at counting shapes and following lines, and does clutter the model can name hurt more than clutter it can't name?

The datasets are the four Shapes/Objects/Lines VQA sets in the `atml-shapes-vqa` Hugging Face organisation. The predictions and methods are fixed in `docs/study3_methodology.pdf` before any model runs.

## Running on Kaggle

GPU T4, internet on, secret `HF_TOKEN` (a read token of an account in the `atml-shapes-vqa` organisation). One notebook cell:

```
!git clone -q https://github.com/zoyakhan51/clutter-vlm /tmp/code && cd /tmp/code && git checkout -q COMMIT
import os; from kaggle_secrets import UserSecretsClient; os.environ["HF_TOKEN"] = UserSecretsClient().get_secret("HF_TOKEN")
!cd /tmp/code && python run_predictions.py --per-version 20
```

Replace `COMMIT` with the commit being run. `--per-version 20` is the trial run (first 20 images of each version). Drop it for the full test-split run. Both run each dataset's official `vqa_scoring.py` on the images they kept.

Outputs go to `/kaggle/working/preds`: one `preds_<dataset>_<model>.csv` per dataset, `scores_*.csv` with per-image scores, and `environment_<model>.json` with the exact versions used.
