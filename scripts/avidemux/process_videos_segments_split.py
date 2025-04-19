#PY  <- Needed to identify #
# Create by tripunto v0.1.3 (2025.04.19)

### Start new process
app=Avidemux(); ed=Editor(); gui=Gui(); app.clearSegments(); app.clearVideoFilters()

### Output file name and directory
out_folder = gui.dirSelect("Select the destination directory") # pop up a dialog asking for a destination directory
out_segment_name = "_cut"
out_ext = "mp4"
out_filename = ""

### Note: Replace lines 15 through 60 with the script from the saved project file.

#adm=Avidemux()
#if not adm.loadVideo("/path/to/file1.mp4"):
#    raise("Cannot load /path/to/file1.mp4")
#if not adm.loadVideo("/path/to/file2.mp4"):
#    raise("Cannot load /path/to/file2.mp4")
#if not adm.loadVideo("/path/to/file3.mp4"):
#    raise("Cannot load /path/to/file3.mp4")
#adm.clearSegments()
#adm.addSegment(1, 294583333, 69833333)
#adm.addSegment(0, 35166666, 14066667)
#adm.addSegment(0, 21100000, 14066666)
#adm.addSegment(1, 217375000, 77124999)
#adm.addSegment(2, 428957550, 54822222)
#adm.addSegment(2, 162024216, 38933334)
#adm.markerA = 175091665
#adm.markerB = 760580558
#adm.setHDRConfig(1, 1, 1, 1, 0)
#adm.videoCodec("x264", "useAdvancedConfiguration=True", "general.params=AQ=25", "general.threads=0", "general.preset=ultrafast", "general.tuning=none", "general.profile=baseline", "general.fast_decode=False", "general.zero_latency=False"
#, "general.fast_first_pass=True", "general.blueray_compatibility=False", "general.fake_interlaced=False", "level=-1", "vui.sar_height=1", "vui.sar_width=1", "vui.overscan=0", "vui.vidformat=5", "vui.fullrange=False"
#, "vui.colorprim=2", "vui.transfer=2", "vui.colmatrix=2", "vui.chroma_loc=0", "MaxRefFrames=3", "MinIdr=25", "MaxIdr=250", "i_scenecut_threshold=40", "intra_refresh=False", "MaxBFrame=3", "i_bframe_adaptive=1"
#, "i_bframe_bias=0", "i_bframe_pyramid=2", "b_deblocking_filter=True", "i_deblocking_filter_alphac0=0", "i_deblocking_filter_beta=0", "cabac=True", "interlaced=False", "constrained_intra=False", "tff=True"
#, "fake_interlaced=False", "analyze.b_8x8=True", "analyze.b_i4x4=True", "analyze.b_i8x8=True", "analyze.b_p8x8=True", "analyze.b_p16x16=False", "analyze.b_b16x16=False", "analyze.weighted_pred=2", "analyze.weighted_bipred=True"
#, "analyze.direct_mv_pred=1", "analyze.chroma_offset=0", "analyze.me_method=1", "analyze.me_range=16", "analyze.mv_range=-1", "analyze.mv_range_thread=-1", "analyze.subpel_refine=7", "analyze.chroma_me=True"
#, "analyze.mixed_references=True", "analyze.trellis=1", "analyze.psy_rd=1.000000", "analyze.psy_trellis=0.000000", "analyze.fast_pskip=True", "analyze.dct_decimate=True", "analyze.noise_reduction=0", "analyze.psy=True"
#, "analyze.intra_luma=11", "analyze.inter_luma=21", "ratecontrol.rc_method=0", "ratecontrol.qp_constant=0", "ratecontrol.qp_min=10", "ratecontrol.qp_max=51", "ratecontrol.qp_step=4", "ratecontrol.bitrate=0"
#, "ratecontrol.rate_tolerance=1.000000", "ratecontrol.vbv_max_bitrate=0", "ratecontrol.vbv_buffer_size=0", "ratecontrol.vbv_buffer_init=1", "ratecontrol.ip_factor=1.400000", "ratecontrol.pb_factor=1.300000"
#, "ratecontrol.aq_mode=1", "ratecontrol.aq_strength=1.000000", "ratecontrol.mb_tree=True", "ratecontrol.lookahead=40")
#adm.addVideoFilter("resampleFps", "mode=0", "newFpsDen=1000", "newFpsNum=25000", "interpolation=0")
#adm.addVideoFilter("crop", "top=0", "bottom=0", "left=32", "right=32", "ar_select=0")
#adm.addVideoFilter("swscale", "width=1280", "height=720", "algo=2", "sourceAR=0", "targetAR=0", "lockAR=True", "roundup=0")
#adm.audioClearTracks()
#adm.setSourceTrackLanguage(0,"und")
#if adm.audioTotalTracksCount() <= 0:
#    raise("Cannot add audio track 0, total tracks: " + str(adm.audioTotalTracksCount()))
#adm.audioAddTrack(0)
#adm.audioCodec(0, "LavAAC", "bitrate=96")
#adm.audioSetMixer(0, "MONO");
#adm.audioSetResample(0, 44100)
#adm.audioSetDrc2(0, 0, 1, 0.001, 0.2, 1, 2, -12)
#adm.audioSetEq(0, 0, 0, 0, 0, 880, 5000)
#adm.audioSetChannelGains(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
#adm.audioSetChannelDelays(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
#adm.audioSetChannelRemap(0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8)
#adm.audioSetShift(0, 0, 0)
#adm.audioSetNormalize2(0, 1, 10, 0)
#adm.setContainer("MP4", "muxerType=0", "optimize=1", "forceAspectRatio=False", "aspectRatio=1", "displayWidth=1280", "rotation=0", "clockfreq=0")

#####################################################################
### Start the process of splitting segments into individual files ###
#####################################################################

nbSeg = ed.nbSegments()
if not nbSeg:
    gui.displayError("Error", "No video loaded, nothing to do, bye")
    return

if nbSeg > 100:
    gui.displayInfo("Warning", "Maximum of 100 segments supported, but got " + str(nbSeg))
    nbSeg = 100

Counter = 0
mark2 = 0
video = {}

for i in range(nbSeg):
	leadingZero = ""
	file_name = ""
	mark1 = mark2
	file_id = ed.getRefIdxForSegment(i)
	file_path = ed.getRefVideoName(file_id)

	if file_path is None:
		gui.displayError("Error", "Cannot obtain reference video file_path")
		return

	### Select auto 'file_name' from video file if 'out_filename' is not defined
	if not out_filename:
		file_name = (splitext(file_path))[0]
		file_name = basename(file_name)
		if file_name is None:
			gui.displayError("Error", "Cannot obtain input basename, include the files and segments from saved project")
			raise("ERROR: Cannot obtain input basename, include the files and segments from saved project")
			return
		if file_id not in video:
			out_cut_number = 1
		else:
			out_cut_number = video[file_id]+1
		video[file_id] = out_cut_number
		if out_cut_number < 10:
			leadingZero = "0"

	### Select 'file_name' for 'out_filename' variable
	else:
		file_name = out_filename
		out_cut_number = str(i+1)
		if i < 10:
			leadingZero = "0"

	### Select segment to file cut process
	mark2 += ed.getDurationForSegment(i)
	print("Segment start:",mark1,"Segment end:",mark2)
	
	app.markerA = mark1
	app.markerB = mark2

	### Save to individual file from segment marks
	output_file = out_folder + "/" + file_name + out_segment_name + leadingZero + str(out_cut_number) + "." + out_ext
	Counter += app.save(output_file)

gui.displayInfo("Finished", str(Counter) + " files out of " + str(nbSeg) + " segments converted")

