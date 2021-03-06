if __name__ == '__main__':
    """
    @Time    :2019/10/8 14:35
    @Author  : 梁家熙
    @Email:  :11849322@mail.sustech.edu.cn
    """
    import json
    from tqdm import tqdm
    import random
    from pprint import pprint
    import os
    import collections
    from typing import List, Dict, Tuple
    import logging

    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    import json
    import shutil
    import sys
    import os
    from allennlp.commands import main

    print('*' * 100)
    print(os.getcwd())
    print()

    config_file = "/home/liangjiaxi/TMP_PROJECT/pingan_event_extraction/using_allennlp/seq2seq/simple_seq2seq.json"

    # Use overrides to train on CPU.
    overrides = json.dumps({
        "trainer": {"cuda_device": 1},
        # 'train_data_path': "/home/liangjiaxi/TMP_PROJECT/pingan_event_extraction/using_allennlp/data/pkuseg_0_test.json",
        # 'validation_data_path': "/home/liangjiaxi/TMP_PROJECT/pingan_event_extraction/using_allennlp/data/pkuseg_0_test.json"
    })

    serialization_dir = "/home/liangjiaxi/TMP_PROJECT/pingan_event_extraction/tmp/seq2seq_debugger"

    # Training will fail if the serialization directory already
    # has stuff in it. If you are running the same training loop
    # over and over again for debugging purposes, it will.
    # Hence we wipe it out in advance.
    # BE VERY CAREFUL NOT TO DO THIS FOR ACTUAL TRAINING!
    shutil.rmtree(serialization_dir, ignore_errors=True)

    # Assemble the command into sys.argv
    sys.argv = [
        "allennlp",  # command name, not used by main
        "train",
        config_file,
        "-s", serialization_dir,
        "--include-package", "using_allennlp",
        "-o", overrides,
        # '--recover'
    ]

    main()