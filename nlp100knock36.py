"""
第4章: 形態素解析
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．

なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

出来上がったコード：
main.py
"""

# coding: utf-8
import MeCab
from collections import Counter
fname = '../input/neko.txt'
fname_parsed = '../output/neko2mecab.txt'


def parse_neko():
    '''「吾輩は猫である」を形態素解析
    「吾輩は猫である」(neko.txt)を形態素解析してneko.txt.mecabに保存する
    '''

    with open(fname) as data_file, \
            open(fname_parsed, mode='w') as out_file:

        mecab = MeCab.Tagger()
        out_file.write(mecab.parse(data_file.read()))


def neco_lines():
    '''「吾輩は猫である」の形態素解析結果のジェネレータ
    「吾輩は猫である」の形態素解析結果を順次読み込んで、各形態素を
    ・表層形（surface）
    ・基本形（base）
    ・品詞（pos）
    ・品詞細分類1（pos1）
    の4つをキーとする辞書に格納し、1文ずつ、この辞書のリストとして返す

    戻り値：
    1文の各形態素を辞書化したリスト
    '''
    with open(fname_parsed) as file_parsed:

        morphemes = []
        for line in file_parsed:

            # 表層形はtab区切り、それ以外は','区切りでバラす
            cols = line.split('\t')
            if(len(cols) < 2):
                return     # 区切りがなければ終了
            res_cols = cols[1].split(',')

            # 辞書作成、リストに追加
            morpheme = {
                'surface': cols[0],
                'base': res_cols[6],
                'pos': res_cols[0],
                'pos1': res_cols[1]
            }
            morphemes.append(morpheme)

            # 品詞細分類1が'句点'なら文の終わりと判定
            if res_cols[1] == '句点':
                yield morphemes
                morphemes = []


# 形態素解析
parse_neko()

# Counterオブジェクトに単語をセット
word_counter = Counter()
for line in neco_lines():
    word_counter.update([morpheme['surface'] for morpheme in line])

# 出現頻度順のリストを取得
list_word = word_counter.most_common()
print(list_word)