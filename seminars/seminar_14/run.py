from omegaconf import DictConfig, OmegaConf
import hydra


@hydra.main(version_base=None)
def run(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))  # {}


if __name__ == "__main__":
    run()
