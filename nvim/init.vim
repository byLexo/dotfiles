syntax on

set number
set sw=2
set expandtab
set smartindent
set rnu
set numberwidth=1
set nowrap
set noswapfile
set nobackup
set incsearch
set encoding=utf-8
set cursorline
set termguicolors

set colorcolumn=120
highlight ColoColumn ctermbg=0 guibg=lightgrey

call plug#begin('~/local/share/nvim/plugged')

" Temas
"Plug 'joshdick/onedark.vim'
Plug 'morhetz/gruvbox'

" Visual
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'


" Modificacion
Plug 'scrooloose/nerdtree'
Plug 'christoomey/vim-tmux-navigator'

call plug#end()

let mapleader = " "

set background=dark
colorscheme gruvbox
let g:gruvbox_contrast_dark = "hard"



nmap <F5> :source ~/.config/nvim/init.vim<CR>
vmap <F5> :source ~/.config/nvim/init.vim<CR>

noremap <up> <nop>
noremap <down> <nop>
noremap <left> <nop>
noremap <right> <nop>

nnoremap <leader>w :w<CR>
nnoremap <silent> <right> :vertical resize +5<CR>
nnoremap <silent> <left> :vertical resize -5<CR>
nnoremap <silent> <up> :resize +5<CR>
nnoremap <silent> <down> :resize -5<CR>
" Me abre el fichero de configuracion
nnoremap <leader>e :e $MYVIMRC<CR>

vnoremap <c-t> :split<CR>:ter<CR>
nnoremap <c-t> :split<CR>:ter<CR>
" Cerrar todos los splits
"map <c-c> <c-w>o

" Moverse al buffer siguiente con <leader> + k
nnoremap <leader>l :bnext<CR>

" Moverse al buffer anterior con <leader> + j
nnoremap <leader>h :bprevious<CR>

" Cerrar el buffer actual con <leader> + q
nnoremap <leader>q :bdelete<CR>

" Crear nueva ventana 
nnoremap <leader>t :tabe<CR>

" Hacer split vertical 
nnoremap <leader>vs :vsp<CR>

" Hacer split horizontal
nnoremap <leader>sp :sp<CR>


" Airline extension
let g:airline#extensions#tabline#enabled = 1  " show open buffers (like tabs)
let g:airline#extensions#tabline#fnamemod = ':t'  " Show only filename
let g:airline_powerline_fonts = 1 " Change separetors to be triangles
let g:airline_theme='tomorrow'


"NERDTree
"autocmd StdinReadPre * let s:std_in=1
"autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
"Keymap of the file browser
let g:NERDTreeChDirMode = 2 "Change the current directory to the current node father
map <leader><tab> :NERDTreeToggle<CR>

let g:NERDTreeDirArrowExpandable = '▸'
let g:NERDTreeDirArrowCollapsible = '▾'

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1] =~# '\s'
endfunction


" tmux navigator
nnoremap <silent> <c-h> :TmuxNavigateLeft<CR>
nnoremap <silent> <c-j> :TmuxNavigateDown<CR>
nnoremap <silent> <c-k> :TmuxNavigateUp<CR>
nnoremap <silent> <c-l> :TmuxNavigateRight<CR>
