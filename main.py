import base64
import binascii
import hashlib
import json

class TextEncryptor:
    def __init__(self):
        # 裏言語変換用の辞書
        self.ura_dict = {
            'あ': 'ぁ', 'い': 'ぃ', 'う': 'ぅ', 'え': 'ぇ', 'お': 'ぉ',
            'か': 'が', 'き': 'ぎ', 'く': 'ぐ', 'け': 'げ', 'こ': 'ご',
            'さ': 'ざ', 'し': 'じ', 'す': 'ず', 'せ': 'ぜ', 'そ': 'ぞ',
            'た': 'だ', 'ち': 'ぢ', 'つ': 'づ', 'て': 'で', 'と': 'ど',
            'は': 'ば', 'ひ': 'び', 'ふ': 'ぶ', 'へ': 'べ', 'ほ': 'ぼ',
            'ア': 'ァ', 'イ': 'ィ', 'ウ': 'ゥ', 'エ': 'ェ', 'オ': 'ォ',
            'カ': 'ガ', 'キ': 'ギ', 'ク': 'グ', 'ケ': 'ゲ', 'コ': 'ゴ',
            'サ': 'ザ', 'シ': 'ジ', 'ス': 'ズ', 'セ': 'ゼ', 'ソ': 'ゾ',
            'タ': 'ダ', 'チ': 'ヂ', 'ツ': 'ヅ', 'テ': 'デ', 'ト': 'ド',
            'ハ': 'バ', 'ヒ': 'ビ', 'フ': 'ブ', 'ヘ': 'ベ', 'ホ': 'ボ'
        }
        
    def scramble(self, text):
        """文字列を暗号化する"""
        # Step 1: MD5ハッシュを生成
        hash_value = hashlib.md5(text.encode()).hexdigest()
        
        # Step 2: 裏言語変換
        ura_text = ''.join(self.ura_dict.get(c, c) for c in text)
        
        # Step 3: Base64エンコード
        base64_text = base64.b64encode(ura_text.encode()).decode()
        
        # Step 4: バイナリ変換（16進数表示）
        hex_text = binascii.hexlify(text.encode()).decode()
        
        # Step 5: すべての要素を組み合わせる
        scrambled = f"{hash_value}:{base64_text}:{hex_text}"
        
        return scrambled

def main():
    encryptor = TextEncryptor()
    
    while True:
        print("\n=== 文字列暗号化プログラム ===")
        text = input("暗号化する文字列を入力してください（終了する場合は 'q' を入力）: ")
        
        if text.lower() == 'q':
            break
            
        scrambled = encryptor.scramble(text)
        print(f"\n暗号化結果:")
        print(scrambled)
        
        # 暗号化結果をファイルに保存するオプション
        save = input("\n暗号化結果をファイルに保存しますか？ (y/n): ")
        if save.lower() == 'y':
            filename = input("保存するファイル名を入力してください: ")
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(scrambled)
            print(f"暗号化結果を {filename} に保存しました。")

if __name__ == "__main__":
    main()