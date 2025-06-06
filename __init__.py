"""Expose ComfyUI node mappings when the repository is placed in ComfyUI's
`custom_nodes` directory."""

from audiox_comfyui import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
