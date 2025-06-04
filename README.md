
---

## 🎭 Fake Mode for Deception Modules

Use `LUNE_MODE=fake` to simulate adversarial perception:

```bash
export LUNE_MODE=fake
python3 -c 'from lune.modules.deception.perception_lens import add_perception_tag, display_tags; add_perception_tag("sandbox-detected"); display_tags()'
