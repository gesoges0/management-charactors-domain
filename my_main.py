import os
import scipy.misc
import numpy as np
from my_model import DCGAN
from my_utils import pp, visualize, to_json, show_all_variables
import argparse
import tensorflow as tf

# os.environ["CUDA_VISIBLE_DEVICES"] = "1"

def main():
    # 画像サイズ設定
    if args.input_width is None:
        args.input_width = args.input_height
    if args.output_width is None:
        args.output_width = args.output_height
    
    # ディレクトリ作成
    if not os.path.exists(args.checkpoint_dir):
        os.makedirs(args.checkpoint_dir)
    if not os.path.exists(args.sample_dir):
        os.makedirs(args.sample_dir)
    
    # gpu 設定
    run_config = tf.ConfigProto()
    run_config.gpu_options.allow_growth=True

    # DCGAN model の宣言
    with tf.Session(config=run_config) as sess:
        dcgan = DCGAN(
            sess,
            input_width=args.input_width, # 入力画像の大きさ
            input_height=args.input_height, 
            output_width=args.output_width, # 出力画像の大きさ
            output_height=args.output_height,
            batch_size=args.batch_size, # バッチサイズ
            sample_num=args.batch_size, # 
            z_dim=args.generate_test_images,
            dataset_name=args.dataset,
            input_fname_pattern=args.input_fname_pattern,
            crop=args.crop,
            checkpoint_dir=args.checkpoint_dir,
            sample_dir=args.sample_dir
        )

        show_all_variables()

        if args.train:
            dcgan.train(args)
        else:
            if not dcgan.load(FLAGS.checkpoint_dir)[0]:
                raise Exception("[!] Train a model first, then run test mode")
        #    
        #OPTION = 1
        #visualize(sess, dcgan, FLAGS, OPTION)

        
    

if __name__ == "__main__":
    # デフォルト値
    default_epoch = 25
    default_learning_rate = 0.0002
    default_beta1 = 0.5
    default_train_size = np.inf
    default_batch_size = 64
    default_input_height = 108
    default_output_height = 64
    default_input_fname_pattern = "*.jpg"
    default_checkpoint_dir = "checkpoint"
    default_sample_dir = "samples"
    default_train = False
    default_crop = False
    default_generate_test_images = 50

    # 引数の設定
    parser = argparse.ArgumentParser()
    parser.add_argument('--epoch', type=int, default=default_epoch, help="epoch to train [{}]".format(default_epoch))
    parser.add_argument('--learning_rate', type=float, default=default_learning_rate, help="learning rate of for adam [{}]".format(default_learning_rate))
    parser.add_argument('--beta1', type=float, default=default_beta1, help="Momentum term of adam [{}]".format(default_beta1))
    parser.add_argument('--train_size', type=float, default=default_train_size, help="The size of train images [{}]".format(default_train_size))
    parser.add_argument('--batch_size', type=int, default=default_batch_size, help="The size of batch images [{}]".format(default_batch_size))
    parser.add_argument('--input_height', type=int, default=default_input_height, help="The size of image to use (will be center cropped). [{}]".format(default_input_height))
    parser.add_argument('--input_width', type=int, default=None, help="The size of image to use (will be center cropped). [{}]".format(default_input_height))
    parser.add_argument('--output_height', type=int, default=default_output_height, help="The size of output image to produce. [{}]".format(default_output_height))
    parser.add_argument('--output_width', type=int, default=None, help="The size of output image to produce. [{}]".format(default_output_height))
    parser.add_argument('--dataset', type=str, default="dataset", help="The name of dataset")
    parser.add_argument('--input_fname_pattern', type=str, default=default_input_fname_pattern, help="Glob pattern of filename of input images [*.jpg]")
    parser.add_argument('--checkpoint_dir', type=str, default=default_checkpoint_dir, help="Directory name to save the checkpoints [{}]".format(default_checkpoint_dir))
    parser.add_argument('--sample_dir', type=str, default=default_sample_dir, help="Directory name to save the image samples [{}]".format(default_sample_dir))
    parser.add_argument('--train', type=bool, default=default_train, help="True for training, False for testing [False]")
    parser.add_argument('--crop', type=bool, default=default_crop, help="True for training, False for testing [False]")    
    parser.add_argument('--generate_test_images',type=int, default=default_generate_test_images, help="Number of images to generate during test. [{}]".format(default_generate_test_images))
    args = parser.parse_args()

    main()




