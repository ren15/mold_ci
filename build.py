from build_base import BuilderBase


class Builder(BuilderBase):

    git_repo = "https://github.com/rui314/mold.git"
    version = "1.0.2"

    def prepare_distro(self):
        self.run("""
        DEBIAN_FRONTEND=noninteractive apt-get update && \
        apt-get install -y build-essential git clang cmake && \
        apt-get install -y libstdc++-10-dev libssl-dev libxxhash-dev zlib1g-dev pkg-config
        """)

    def clean(self):
        self.run("rm -rf mold")

    def source(self):
        self.run(f"git clone {self.git_repo}")

    def build(self):
        self.run(f"""
        cd mold && \
        git checkout v{self.version} && \
        make -j$(nproc) CXX=clang++
        """)


def main():
    builder = Builder()

    builder.prepare_distro()
    builder.clean()
    builder.source()
    builder.build()


if __name__ == '__main__':
    main()
