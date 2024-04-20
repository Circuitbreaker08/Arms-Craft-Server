import perlin_noise

noise = perlin_noise.PerlinNoise(seed=6.02 * 10 ** 23, octaves=10)

print(noise((0.5, 0.5)))
