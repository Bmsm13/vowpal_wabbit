import os


def corrigir_upload_artifact(path_base="."):
    for root, dirs, files in os.walk(path_base):
        for nome_arquivo in files:
            if nome_arquivo.endswith((".yml", ".yaml")):
                caminho_completo = os.path.join(root, nome_arquivo)
                with open(caminho_completo, "r", encoding="utf-8") as f:
                    conteudo = f.read()

                if "actions/upload-artifact@v1" in conteudo:
                    novo_conteudo = conteudo.replace(
                        "actions/upload-artifact@v1", "actions/upload-artifact@v3"
                    )
                    with open(caminho_completo, "w", encoding="utf-8") as f:
                        f.write(novo_conteudo)
                    print(f"✅ Corrigido: {caminho_completo}")


if __name__ == "__main__":
    corrigir_upload_artifact(".")
