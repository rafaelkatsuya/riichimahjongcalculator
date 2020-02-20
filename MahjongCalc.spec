# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['MahjongCalc.py'],
             pathex=['C:\\Users\\rafae\\PycharmProjects\\MajongCalc'],
             binaries=[],
             datas=[],
             hiddenimports=['readline', 'org', 'fcntl', 'riscosenviron', 'riscospath', 'riscos', 'ce', '_emx_link', 'os2', 'pwd', 'posix', 'resource', 'org.python', 'PyQt5' ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MahjongCalc',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
