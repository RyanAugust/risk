import pygame

from risk import logger
import risk.graphics
import risk.graphics.assets.text
import risk.graphics.input
import risk.graphics.picasso
import risk.player
from risk.graphics.assets.text import TextAsset
from risk.graphics.input import attack_phase, fortify_phase, reinforce_phase, handle_user_mouse_input
from risk.graphics.picasso import get_picasso
from risk.player import HumonRiskPlayer

LAYER = '5_player_feedback'


class HumonGuiRiskPlayer(HumonRiskPlayer):
    def __init__(self, name):
        HumonRiskPlayer.__init__(self, name)

    def reinforce(self, game_master):
        #self.reserves = 0
        # for territory in game_master.player_territories(self).values():
        #    territory.armies = 100
        #picasso = get_picasso()
        #phase_asset = TextAsset(400, 600, 'reinforcing...')
        #picasso.add_asset(LAYER, phase_asset)
        logger.debug("starting reinforcement phase")
        handle_user_mouse_input(game_master,
                                reinforce_phase)

    def attack(self, game_master):
        logger.debug("starting attack phase")
        # phase_asset.render_text('attacking...')
        handle_user_mouse_input(game_master, attack_phase)

    def fortify(self, game_master):
        logger.debug("starting fortify phase")
        # phase_asset.render_text('fortifying...')
        handle_user_mouse_input(game_master, fortify_phase)
        logger.debug("GUI player finished turn!")
        #picasso.remove_asset(LAYER, phase_asset)
