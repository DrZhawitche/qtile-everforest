call plug#begin()

Plug 'sainnhe/everforest'
Plug 'preservim/nerdtree'
Plug 'vim-airline/vim-airline'
Plug 'dmerejkowsky/vim-ale'
Plug 'Raimondi/delimitMate'
Plug 'farmergreg/vim-lastplace'
Plug 'ap/vim-css-color'
Plug 'tpope/vim-commentary'
Plug 'tpope/vim-surround'

call plug#end()

if has('termguicolors')
	set termguicolors
endif
set background=dark
colorscheme everforest
let g:everforest_background = 'medium'

syntax on
set number relativenumber
set ruler
set backspace=indent,eol,start
set showcmd
set incsearch
set hlsearch
set tabstop=4

set mouse=a

" Fixing typos
command W w
command Q q

" Moving through lines individually
map j gj
map k gk

" Automatically recompile when editing a config.h
" autocmd BufWritePost config.h,config.def.h !sudo make install
