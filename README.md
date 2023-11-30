# image server

## セットアップ

```
poetry install
```

<details>
<summary>Raspberry Piで、pillowのインストールに失敗する場合</summary>

- 以下のコマンドを実行して、必要な依存関係をインストールする
  ```bash
  sudo apt-get update
  sudo apt-get install libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7 libtiff5
  ```

</details>

## 起動

```
poetry run uvicorn image_server.main:app --reload
```