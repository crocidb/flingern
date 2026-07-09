{
  description = "flingern - static website generator for art photographers";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      forAllSystems = nixpkgs.lib.genAttrs [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];
    in {
      devShells = forAllSystems (system:
        let pkgs = nixpkgs.legacyPackages.${system};
        in {
          default = pkgs.mkShell {
            packages = with pkgs; [
              python3
              uv
              libjpeg
              zlib
            ];

            shellHook = ''
              echo "flingern development shell"

              export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [
                pkgs.libjpeg
                pkgs.zlib
              ]}:$LD_LIBRARY_PATH
            '';
          };
        });
    };
}
