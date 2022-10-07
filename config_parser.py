import configargparse


def config_parser():
    parser = configargparse.ArgumentParser()
    parser.add_argument('--config', is_config_file=True,
                        help='config file path')
    parser.add_argument("--prefix", type=str, default='',
                        help='input data directory')
    parser.add_argument("--datadir", type=str,
                        help='input data directory')
    parser.add_argument("--expdir", type=str,
                        help='where to store ckpts and logs')
    parser.add_argument("--expname", type=str,
                        help='experiment name')
    parser.add_argument("--seed", type=int, default=666,
                        help='random seed')
    parser.add_argument("--factor", type=int, default=8,
                        help='downsample factor for LLFF images')
    parser.add_argument("--bd_factor", type=float, default=0.75, help='expand factor of the ROI box')
    parser.add_argument("--chunk", type=int, default=1024 * 32,
                        help='number of rays processed in parallel, decrease if running out of memory')
    parser.add_argument("--fp16", action='store_true',
                        help='use half precision to train')

    # for MPV only, not used for MPMesh
    parser.add_argument("--mpv_frm_num", type=int, default=90,
                        help='frame number of the mpv')
    parser.add_argument("--mpv_isloop", action='store_true',
                        help='produce looping videos')
    parser.add_argument("--init_from", type=str, default='',
                        help='path to ckpt, will add prefix, currently only support reload from MPI')
    parser.add_argument("--init_std", type=float, default=0,
                        help='noise std of the dynamic MPV')

    # loss config
    parser.add_argument("--loss_ref_idx", type=str, default='0',
                        help='a,b,c swd_alpha = ref if view==swd_alpha_reference_viewidx else other')
    parser.add_argument("--loss_name", type=str, default='gpnn',
                        help='gpnn, mse, swd, avg. gpnn_x to specify alpha==x')
    parser.add_argument("--loss_name_ref", type=str, default='gpnn',
                        help='gpnn, mse, swd, avg. gpnn_x to specify alpha==x')
    parser.add_argument("--swd_macro_block", type=int, default=65,
                        help='used for gpnn low mem')
    parser.add_argument("--swd_patch_size", type=int, default=5,
                        help='produce looping videos')
    parser.add_argument("--swd_patch_size_ref", type=int, default=5,
                        help='produce looping videos')
    parser.add_argument("--swd_patcht_size", type=int, default=5,
                        help='produce looping videos')
    parser.add_argument("--swd_patcht_size_ref", type=int, default=5,
                        help='produce looping videos')
    parser.add_argument("--swd_stride", type=int, default=2,
                        help='produce looping videos')
    parser.add_argument("--swd_stride_ref", type=int, default=2,
                        help='produce looping videos')
    parser.add_argument("--swd_stridet", type=int, default=2,
                        help='produce looping videos')
    parser.add_argument("--swd_stridet_ref", type=int, default=2,
                        help='produce looping videos')
    parser.add_argument("--swd_rou", type=str, default='0',
                        help='parameter of robustness term, can also be mse, abs')
    parser.add_argument("--swd_rou_ref", type=str, default='0',
                        help='parameter of robustness term')
    parser.add_argument("--swd_scaling", type=float, default=0.2,
                        help='parameter of robustness term')
    parser.add_argument("--swd_scaling_ref", type=float, default=0.2,
                        help='parameter of robustness term')
    parser.add_argument("--swd_alpha", type=float, default=0,
                        help='alpha, bigger than 100 is equivalent to None')
    parser.add_argument("--swd_alpha_ref", type=float, default=0,
                        help='alpha, bigger than 100 is equivalent to None')
    parser.add_argument("--swd_dist_fn", type=str, default='mse',
                        help='alpha, bigger than 100 is equivalent to None')
    parser.add_argument("--swd_dist_fn_ref", type=str, default='mse',
                        help='alpha, bigger than 100 is equivalent to None')
    parser.add_argument("--swd_loss_gain_ref", type=float, default=1,
                        help='alpha, bigger than 100 is equivalent to None')

    # pyramid configuration
    parser.add_argument("--pyr_stage", type=str, default='',
                        help='x,y,z,...   iteration to upsample')
    parser.add_argument("--pyr_minimal_dim", type=int, default=60,
                        help='if > 0, will determine the pyr_stage')
    parser.add_argument("--pyr_num_epoch", type=int, default=600,
                        help='iter num in each level')
    parser.add_argument("--pyr_factor", type=float, default=0.5,
                        help='factor in each pyr level')
    parser.add_argument("--swd_num_proj", type=int, default=128,
                        help='produce looping videos')

    # for mpi
    parser.add_argument("--sparsify_epoch", type=int, default=-1,
                        help='sparsify the MPMesh in epoch')
    parser.add_argument("--sparsify_rmfirstlayer", action='store_true',
                        help='if true, will remove the first layer')
    parser.add_argument("--sparsify_erode", type=int, default=2,
                        help='iters to dilate the alpha channel')
    parser.add_argument("--learn_loop_mask", action='store_true',
                        help='if true, will learn a loop_mask jointly')

    parser.add_argument("--direct2sh_epoch", type=int, default=-1,
                        help='converting direct to sh')
    parser.add_argument("--sparsify_alpha_thresh", type=float, default=0.03,
                        help='alpha thresh for sparsify')
    parser.add_argument("--vid2img_mode", type=str, default='average',
                        help='choose among average, median, static, dynamic')
    parser.add_argument("--mpi_h_scale", type=float, default=1,
                        help='the height of the stored MPI is <mpi_h_scale * H>')
    parser.add_argument("--mpi_w_scale", type=float, default=1,
                        help='the width of the stored MPI is <mpi_w_scale * W>')
    parser.add_argument("--mpi_h_verts", type=int, default=12,
                        help='the height of the stored MPI is <mpi_h_scale * H>')
    parser.add_argument("--mpi_w_verts", type=int, default=15,
                        help='the width of the stored MPI is <mpi_w_scale * W>')
    parser.add_argument("--mpi_d", type=int, default=64,
                        help='number of the MPI layer')
    parser.add_argument("--atlas_grid_h", type=int, default=8,
                        help='atlas_grid_h * atlas_grid_w == mpi_d')
    parser.add_argument("--atlas_size_scale", type=float, default=1,
                        help='atlas_size = mpi_d * H * W * atlas_size_scale')
    parser.add_argument("--atlas_cnl", type=int, default=4,
                        help='channel num')
    parser.add_argument("--multires_views", type=int, default=0,
                        help='log2 of max freq for positional encoding (2D direction)')
    parser.add_argument("--model_type", type=str, default="MPI",
                        choices=["MPI", "MPMesh"])
    parser.add_argument("--rgb_mlp_type", type=str, default='direct',
                        help='mlp type, choose among "direct", "rgbamlp", "rgbmlp"')
    parser.add_argument("--rgb_activate", type=str, default='sigmoid',
                        help='activate function for rgb output, choose among "none", "sigmoid"')
    parser.add_argument("--alpha_activate", type=str, default='sigmoid',
                        help='activate function for rgb output, choose among "none", "sigmoid"')
    parser.add_argument("--optimize_depth", action='store_true',
                        help='if true, optimzing the depth of each plane')
    parser.add_argument("--optimize_normal", action='store_true',
                        help='if true, optimzing the normal of each plane')
    parser.add_argument("--optimize_geo_start", type=int, default=10000000,
                        help='iteration to start optimizing verts and uvs')
    parser.add_argument("--optimize_verts_gain", type=float, default=1,
                        help='set 0 to disable the vertices optimization')
    parser.add_argument("--optimize_uvs_gain", type=float, default=1,
                        help='set 0 to disable the uvs optimization')
    parser.add_argument("--normalize_verts", action='store_true',
                        help='if true, the parameter is normalized')

    # about training
    parser.add_argument("--upsample_stage", type=str, default="",
                        help='x,y,z,...  stage to perform upsampling')
    parser.add_argument("--rgb_smooth_loss_weight", type=float, default=0,
                        help='rgb smooth loss')
    parser.add_argument("--a_smooth_loss_weight", type=float, default=0,
                        help='rgb smooth loss')
    parser.add_argument("--d_smooth_loss_weight", type=float, default=0,
                        help='depth smooth loss')
    parser.add_argument("--laplacian_loss_weight", type=float, default=0,
                        help='as rigid as possible smooth loss')
    parser.add_argument("--density_loss_weight", type=float, default=0,
                        help='density loss')

    # training options
    parser.add_argument("--N_iters", type=int, default=30)
    parser.add_argument("--optimizer", type=str, default='adam', choices=['adam', 'sgd'],
                        help='optmizer')
    parser.add_argument("--netdepth", type=int, default=8,
                        help='layers in network')
    parser.add_argument("--netwidth", type=int, default=256,
                        help='channels per layer')
    parser.add_argument("--patch_h_size", type=int, default=512,
                        help='batch size (number of random rays per gradient step)')
    parser.add_argument("--patch_w_size", type=int, default=512,
                        help='batch size (number of random rays per gradient step)')
    parser.add_argument("--patch_h_stride", type=int, default=128,
                        help='batch size (number of random rays per gradient step)')
    parser.add_argument("--patch_w_stride", type=int, default=128,
                        help='batch size (number of random rays per gradient step)')
    parser.add_argument("--netchunk", type=int, default=1024*64,
                        help='number of pts sent through network in parallel, decrease if running out of memory')
    parser.add_argument("--lrate", type=float, default=5e-4,
                        help='learning rate')
    parser.add_argument("--lrate_adaptive", action='store_true',
                        help='adaptively adjust learning rate based on patch size')
    parser.add_argument("--lrate_decay", type=int, default=30,
                        help='exponential learning rate decay (in 1000 steps)')

    # rendering options
    parser.add_argument("--perturb", type=float, default=1.,
                        help='set to 0. for no jitter, 1. for jitter')
    parser.add_argument("--raw_noise_std", type=float, default=1e0,
                        help='std dev of noise added to regularize sigma_a output, 1e0 recommended')
    parser.add_argument("--render_only", action='store_true',
                        help='do not optimize, reload weights and render out render_poses path')
    parser.add_argument("--render_view", type=int, default=-1,
                        help='do not optimize, reload weights and render out render_poses path')
    parser.add_argument("--render_test", action='store_true',
                        help='do not optimize, reload weights and render out render_poses path')
    parser.add_argument("--render_factor", type=float, default=1,
                        help='change the keypoint location')

    # logging options
    parser.add_argument("--i_img",    type=int, default=300,
                        help='frequency of tensorboard image logging')
    parser.add_argument("--i_print",   type=int, default=300,
                        help='frequency of console printout and metric loggin')
    parser.add_argument("--i_weights", type=int, default=20000,
                        help='frequency of weight ckpt saving')
    parser.add_argument("--i_testset", type=int, default=2000000000,
                        help='frequency of testset saving')
    parser.add_argument("--i_eval", type=int, default=1000000000,
                        help='frequency of testset saving')
    parser.add_argument("--i_video",   type=int, default=10000,
                        help='frequency of render_poses video saving')

    # multiprocess learning
    parser.add_argument("--gpu_num", type=int, default='-1', help='number of processes')

    # test use latent_t
    parser.add_argument("--optimize_poses", default=False, action='store_true',
                        help='optimize poses')
    parser.add_argument("--optimize_poses_start", type=int, default=0, help='start step of optimizing poses')
    parser.add_argument("--surpress_boundary_thickness", type=int, default=0,
                        help='do not supervise the boundary of thickness <>, 0 to disable')

    ## For other losses
    parser.add_argument("--sparsity_loss_weight", type=float, default=0,
                        help='sparsity loss weight')
    return parser
