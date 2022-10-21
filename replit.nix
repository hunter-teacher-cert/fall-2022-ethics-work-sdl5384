{ pkgs }: {
    deps = [
        pkgs.python39Packages.pip
        pkgs.pip install selenium
        pkgs.cowsay
    ];
}