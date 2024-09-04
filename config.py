# from petals.constants import PUBLIC_INITIAL_PEERS

from data_structures import ModelInfo

# INITIAL_PEERS = PUBLIC_INITIAL_PEERS

INITIAL_PEERS = ['/ip4/3.15.176.189/tcp/31337/p2p/12D3KooWLAFTzvgw5pD2UgrTY1aNQjqrvNqZPMF3nyLMAMZGYGyw']

MODELS = [
    # ModelInfo(
    #     dht_prefix="Llama-2-7B-bf16-sharded-hf",
    #     repository="https://huggingface.co/TinyPixel/Llama-2-7B-bf16-sharded",
    #     num_blocks=32,
    # ),
    ModelInfo(
        dht_prefix="bigscience/bloom-560m-petals",
        repository="https://huggingface.co/bigscience/bloom-560m",
        num_blocks=24,
    ),
    # ModelInfo(
    #     dht_prefix="StableBeluga2-hf",
    #     repository="https://huggingface.co/petals-team/StableBeluga2",
    #     num_blocks=80,
    # ),
    # ModelInfo(
    #     dht_prefix="falcon-180B-chat",
    #     repository="https://huggingface.co/tiiuae/falcon-180B-chat",
    #     num_blocks=80,
    #     limited=True,
    # ),
    # ModelInfo(
    #     dht_prefix="Llama-2-70b-chat-hf",
    #     repository="https://huggingface.co/meta-llama/Llama-2-70b-chat-hf",
    #     num_blocks=80,
    # ),
    # ModelInfo(
    #     dht_prefix="Llama-2-70b-hf",
    #     repository="https://huggingface.co/meta-llama/Llama-2-70b-hf",
    #     num_blocks=80,
    # ),
]

UPDATE_PERIOD = 60