Title: The Ultimate Vim Configuration
Date: 2020-05-07 18:48
Modified: 2020-05-07 18:48
Category: All 
Tags: Vim, TextEditor
Slug: found-out-the-ultimate-vim-configurations
Authors: Shiva Saxena
Summary: Are you a Vim user, and searching for some awesome tweaks that would make your text editing more efficient and delightful? If yes, then I would like to share with you the ultimate vim configurations that I found out recently.
Header_Cover: images/my-post-bg.jpg
Og_Image: images/my-contact-bg.jpg
Twitter_Image: images/my-contact-bg.jpg


Greetings!

Are you a Vim user, and searching for some awesome tweaks that would make your text editing more efficient and delightful? If yes, then I would like to share with you [The Ultimate Vim Configuration](https://github.com/amix/vimrc). The tweaks are so awesome, that I couldn't resist myself from sharing it on the blog.

The detailed documentation of the repo is already well written, and if you are a vim user then you can also make some of your custom tweaks if you want. In this, you get the availability of so many plugins at one place, configured optimized, and ease of extendability of your custom tweaks. Along with it, the installation/uninstallation process doesn't take more than 1-2 minutes.

After installations, I included some of my custom configurations as follows:

```shell
    set nu

    map <C-m> :tabnext<cr>

    let MRU_Open_File_Use_Tabs = 1

    let g:ctrlp_prompt_mappings = {
        \ 'AcceptSelection("e")': ['<2-LeftMouse>'],
        \ 'AcceptSelection("t")': ['<cr>'],
        \ }

    colorscheme gruvbox
    highlight Normal ctermbg=16
    set colorcolumn=80
    highlight colorcolumn ctermbg=black


    let g:NERDTreeWinSize=30


    let g:gitgutter_terminal_reports_focus=0
    set updatetime=100 

    let g:gitgutter_enabled=1
```

Overall, it is working like a charm for me! You may try it yourself if you wish to.

That's all for now, thanks for reading!

See you in the next post :)

### References
- The Ultimate Vim Configuration: [github.com/amix/vimrc](https://github.com/amix/vimrc)
