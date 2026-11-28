# Heyyy! It's Varunika Rai <3

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=19&pause=1000&color=F7A8C4&center=true&vCenter=true&width=700&lines=Heyy!+It's+Varunika+Rai+<3;Aspiring+AI+Engineer;Machine+Learning+Developer;Building+Thoughtfully" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-F7A8C4?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/PyTorch-2.x-C8A2C8?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch" />
  <img src="https://img.shields.io/badge/Focus-AI%20%2F%20ML-F7A8C4?style=flat-square" alt="Focus" />
  <img src="https://komarev.com/ghpvc/?username=varunikarai&color=F7A8C4" alt="Profile Views" />
</p>

## About Me

I’m an aspiring AI and machine learning developer focused on building practical projects and learning through real implementation. I enjoy exploring the ideas behind modern ML systems rather than treating them as black boxes.

## Current Focus

- Deep Learning
- LLM Applications
- RAG Systems
- AI Engineering
- Open Source (anomalib, sbi, QuTiP)

## Tech Stack

| Languages | AI / ML | Frameworks | Developer Tools |
|---|---|---|---|
| Python • C++ • SQL • JavaScript | PyTorch • NumPy • Pandas • Scikit-Learn • OpenCV | React • Vite • HTML • CSS | Git • GitHub • VS Code • PyCharm • Linux |

## GitHub Stats

<p align="center">
  <img src="https://streak-stats.demolab.com?user=varunikarai&theme=dark&hide_border=true&background=0D1117&ring=F7A8C4&fire=F7A8C4&currStreakLabel=F7A8C4&v=1" alt="GitHub Streak" />
</p>

## Recent Activity

<!-- ACTIVITY:START -->

_Updated automatically on 2026-11-29 (IST) from public GitHub activity._

**Merged pull requests:** 3, across anomalib, qutip, sbi.

- 2026-11-17 · [qutip/qutip #3070](https://github.com/qutip/qutip/pull/3070): Document the hbar = 1 convention of the solvers
- 2026-10-27 · [sbi-dev/sbi #2085](https://github.com/sbi-dev/sbi/pull/2085): fix: bin TARP coverage values over [0, 1]
- 2026-10-27 · [open-edge-platform/anomalib #3853](https://github.com/open-edge-platform/anomalib/pull/3853): fix(model): keep PatchCore's batch size dynamic when exporting

**Last 30 days:** 2 commits · 1 pull request · 1 issue · 0 reviews, in [open-edge-platform/anomalib](https://github.com/open-edge-platform/anomalib), [qutip/qutip](https://github.com/qutip/qutip), [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy).

<!-- ACTIVITY:END -->

## Open Source

| Project | Details |
|---|---|
| anomalib <br> OpenVINO Toolkit (Intel) | Fix for exported PatchCore models only accepting a batch of exactly 2 images (ONNX and OpenVINO input fixed at `[2, 3, H, W]`), requested by a user in [#3726](https://github.com/open-edge-platform/anomalib/issues/3726). The fix keeps the batch dimension dynamic while exporting, so single-image inference works again. Merged 2026-10-27. <br> ![PR #3853](https://img.shields.io/github/pulls/detail/state/open-edge-platform/anomalib/3853?style=flat-square&label=PR%20%233853) ![Python](https://img.shields.io/badge/Python-F7A8C4?style=flat-square&logo=python&logoColor=white) ![OpenVINO](https://img.shields.io/badge/OpenVINO-C8A2C8?style=flat-square&logo=intel&logoColor=white) <br> [Pull request](https://github.com/open-edge-platform/anomalib/pull/3853) |
| sbi <br> sbi-dev (simulation-based inference) | Fix for the TARP coverage diagnostic: coverage values were binned over their own range instead of `[0, 1]`, so a truncated grid biased the ATC statistic and the KS p-value. The fix bins them over `[0, 1]`. Merged 2026-10-27. <br> ![PR #2085](https://img.shields.io/github/pulls/detail/state/sbi-dev/sbi/2085?style=flat-square&label=PR%20%232085) ![Python](https://img.shields.io/badge/Python-F7A8C4?style=flat-square&logo=python&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-C8A2C8?style=flat-square&logo=pytorch&logoColor=white) <br> [Pull request](https://github.com/sbi-dev/sbi/pull/2085) |
| anomalib <br> OpenVINO Toolkit (Intel) | Fix for [#3726](https://github.com/open-edge-platform/anomalib/issues/3726): an exported PatchCore model scored defects differently from its own checkpoint, because `predict` silently kept the constructor's arguments while `export` restored the checkpoint's. The fix warns when the two differ. Root cause confirmed by the reporter on their data. <br> ![PR #3846](https://img.shields.io/github/pulls/detail/state/open-edge-platform/anomalib/3846?style=flat-square&label=PR%20%233846) ![Python](https://img.shields.io/badge/Python-F7A8C4?style=flat-square&logo=python&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-C8A2C8?style=flat-square&logo=pytorch&logoColor=white) <br> [Pull request](https://github.com/open-edge-platform/anomalib/pull/3846) |
| anomalib <br> OpenVINO Toolkit (Intel) | Fix for the remaining score gap in [#3726](https://github.com/open-edge-platform/anomalib/issues/3726): exported models (Torch, ONNX, OpenVINO) resized the input without antialiasing while `Engine.predict` resized with it, so on images larger than the model input the exported model scored differently from its own checkpoint. The fix keeps antialiasing in the exported pre-processing, closing the Torch to ONNX gap from 0.0429 to 0.0000. <br> ![PR #3882](https://img.shields.io/github/pulls/detail/state/open-edge-platform/anomalib/3882?style=flat-square&label=PR%20%233882) ![Python](https://img.shields.io/badge/Python-F7A8C4?style=flat-square&logo=python&logoColor=white) ![ONNX](https://img.shields.io/badge/ONNX-C8A2C8?style=flat-square&logo=onnx&logoColor=white) <br> [Pull request](https://github.com/open-edge-platform/anomalib/pull/3882) |
| QuTiP <br> Quantum Toolbox in Python | Docs for [#1360](https://github.com/qutip/qutip/issues/1360): states that the solvers work in units where ħ = 1, in the `sesolve` and `mesolve` docstrings and in a note in the master equation guide. <br> ![PR #3070](https://img.shields.io/github/pulls/detail/state/qutip/qutip/3070?style=flat-square&label=PR%20%233070) ![Python](https://img.shields.io/badge/Python-F7A8C4?style=flat-square&logo=python&logoColor=white) ![Docs](https://img.shields.io/badge/Docs-C8A2C8?style=flat-square) <br> [Pull request](https://github.com/qutip/qutip/pull/3070) |

## Featured Projects

| Project | Details |
|---|---|
| BeyondHorizons_Agrisense | AI-driven project focused on practical problem solving. <br> ![Python](https://img.shields.io/badge/Python-F7A8C4?style=flat-square&logo=python&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-C8A2C8?style=flat-square&logo=pytorch&logoColor=white) <br> [Repository](https://github.com/varunikarai/BeyondHorizons_Agrisense) |
| Papertrail Assignment | Structured exploration of applied machine learning concepts. <br> ![Python](https://img.shields.io/badge/Python-F7A8C4?style=flat-square&logo=python&logoColor=white) ![ML](https://img.shields.io/badge/ML-C8A2C8?style=flat-square) <br> [Repository](https://github.com/varunikarai/PaperTrail) |
| UBTAN Salon Website | A polished front-end project with a calm, modern feel. <br> ![React](https://img.shields.io/badge/React-C8A2C8?style=flat-square&logo=react&logoColor=white) ![CSS](https://img.shields.io/badge/CSS-F7A8C4?style=flat-square&logo=css3&logoColor=white) <br> [Repository](https://github.com/varunikarai/UBTAN-Salon) |


## Connect

- GitHub: [varunikarai](https://github.com/varunikarai)
- LinkedIn: [varunikarai](https://www.linkedin.com/in/varunikarai)
- Discord: vero_40315
- Email: [itsvarunikarai@gmail.com](mailto:itsvarunikarai@gmail.com)

## Contribution Snake

<p align="center">
  <img src="assets/github-contribution-grid-snake.svg" alt="Contribution Snake" />
</p>

---

Thanks for stopping by.

Happy Building ✨
