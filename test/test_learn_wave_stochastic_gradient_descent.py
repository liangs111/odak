import sys
import odak
import torch


def test():
    device = torch.device('cpu') # (1)
    target = odak.learn.tools.load_image('./test/usaf1951.png', normalizeby = 255., torch_style = True)[1] # (4)
    hologram, reconstruction = odak.learn.wave.stochastic_gradient_descent(
                                                                           target,
                                                                           wavelength = 532e-9,
                                                                           distance = 20e-2,
                                                                           pixel_pitch = 8e-6,
                                                                           propagation_type = 'Bandlimited Angular Spectrum',
                                                                           n_iteration = 50,
                                                                           learning_rate = 0.1
                                                                          ) # (2)
    odak.learn.tools.save_image(
                                'phase.png', 
                                odak.learn.wave.calculate_phase(hologram) % (2 * odak.pi), 
                                cmin = 0., 
                                cmax = 2 * odak.pi
                               ) # (3)
    odak.learn.tools.save_image('target.png', target, cmin = 0., cmax = 1.)
    odak.learn.tools.save_image(
                                'reconstruction.png', 
                                odak.learn.wave.calculate_amplitude(reconstruction) ** 2, 
                                cmin = 0., 
                                cmax = 1.
                               )
    assert True == True


if __name__ == '__main__':
    sys.exit(test())
