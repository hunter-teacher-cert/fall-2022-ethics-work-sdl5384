{ pkgs }: {
    deps = [
        pkgs.pip install selenium
        pkgs.cowsay
    ];
}