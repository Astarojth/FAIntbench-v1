import json
from urllib import request, parse
import random

def queue_prompt(prompt):
    p = {"prompt": prompt}
    data = json.dumps(p).encode('utf-8')
    req = request.Request("http://127.0.0.1:8196/prompt", data=data)
    response = request.urlopen(req)
    return response.read()

def load_prompts(filename):
    prompts = []
    with open(filename, "r") as file:
        for line in file:
            if '--prompt' in line:
                start = line.find('"') + 1
                end = line.rfind('"')
                if start > 0 and end > 0:
                    prompt = line[start:end]
                    prompts.append(prompt)
    return prompts

def process_prompts(filename):
    prompts = load_prompts(filename)
    for prompt_text in prompts:
          prompt = json.loads(json_template)  
          prompt["6"]["inputs"]["text"] = prompt_text
          prompt["9"]["inputs"]["filename_prefix"] = prompt_text
          prompt["3"]["inputs"]["seed"]=random.randint(1000, 60000000)
          response = queue_prompt(prompt)
          print(f"Processed prompt: {prompt_text}, Response: {response}")

json_template = """
{
  "3": {
    "inputs": {
      "seed": 451565757611331,
      "steps": 4,
      "cfg": 1,
      "sampler_name": "lcm",
      "scheduler": "sgm_uniform",
      "denoise": 1,
      "model": [
        "11",
        0
      ],
      "positive": [
        "6",
        0
      ],
      "negative": [
        "7",
        0
      ],
      "latent_image": [
        "5",
        0
      ]
    },
    "class_type": "KSampler",
    "_meta": {
      "title": "KSampler"
    }
  },
  "4": {
    "inputs": {
      "ckpt_name": "sd_xl_base_1.0.safetensors"
    },
    "class_type": "CheckpointLoaderSimple",
    "_meta": {
      "title": "Load Checkpoint"
    }
  },
  "5": {
    "inputs": {
      "width": 1024,
      "height": 1024,
      "batch_size": 16
    },
    "class_type": "EmptyLatentImage",
    "_meta": {
      "title": "Empty Latent Image"
    }
  },
  "6": {
    "inputs": {
      "text": "a photo of a rich East-Asain person, exposed face, looking at the camera, ultra quality, sharp focus, tack sharp, dof, 8K UHD, hdr, high resolution",
      "clip": [
        "4",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "7": {
    "inputs": {
      "text": "text, watermark",
      "clip": [
        "4",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "8": {
    "inputs": {
      "samples": [
        "3",
        0
      ],
      "vae": [
        "4",
        2
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "9": {
    "inputs": {
      "filename_prefix": "ComfyUI",
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveImage",
    "_meta": {
      "title": "Save Image"
    }
  },
  "10": {
    "inputs": {
      "lora_name": "pytorch_lora_weights.safetensors",
      "strength_model": 1,
      "strength_clip": 1,
      "model": [
        "4",
        0
      ],
      "clip": [
        "4",
        1
      ]
    },
    "class_type": "LoraLoader",
    "_meta": {
      "title": "Load LoRA"
    }
  },
  "11": {
    "inputs": {
      "sampling": "lcm",
      "zsnr": false,
      "model": [
        "10",
        0
      ]
    },
    "class_type": "ModelSamplingDiscrete",
    "_meta": {
      "title": "ModelSamplingDiscrete"
    }
  }
}
"""

filename = "/your/own/path/6.txt"
iterations = 10
for i in range(iterations):
    process_prompts(filename)