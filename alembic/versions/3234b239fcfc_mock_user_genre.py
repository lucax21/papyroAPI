"""mock user_genre

Revision ID: 3234b239fcfc
Revises: 526c1a7b2d84
Create Date: 2022-07-28 19:36:43.625735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3234b239fcfc'
down_revision = '526c1a7b2d84'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('''
    INSERT INTO user_genre(fk_genre, fk_user)
    VALUES (5, 272),
            (5, 304),
            (6, 219),
            (2, 456),
            (5, 51),
            (1, 282),
            (1, 384),
            (5, 378),
            (6, 187),
            (6, 300),
            (1, 369),
            (5, 499),
            (4, 285),
            (4, 88),
            (4, 341),
            (9, 356),
            (10, 475),
            (4, 343),
            (1, 492),
            (4, 483),
            (7, 451),
            (10, 304),
            (1, 295),
            (10, 490),
            (7, 353),
            (5, 432),
            (4, 237),
            (8, 159),
            (4, 185),
            (9, 205),
            (6, 295),
            (2, 264),
            (1, 264),
            (1, 273),
            (9, 99),
            (1, 136),
            (5, 200),
            (9, 44),
            (9, 434),
            (4, 450),
            (2, 213),
            (2, 281),
            (10, 372),
            (5, 144),
            (1, 382),
            (7, 266),
            (1, 371),
            (4, 269),
            (4, 460),
            (4, 45),
            (4, 150),
            (6, 310),
            (5, 451),
            (1, 316),
            (1, 495),
            (5, 436),
            (8, 46),
            (7, 98),
            (5, 443),
            (9, 494),
            (10, 271),
            (6, 432),
            (4, 266),
            (2, 371),
            (10, 105),
            (1, 138),
            (7, 482),
            (2, 363),
            (7, 127),
            (6, 54),
            (6, 484),
            (3, 18),
            (8, 11),
            (9, 491),
            (8, 129),
            (9, 300),
            (7, 394),
            (4, 219),
            (6, 100),
            (9, 332),
            (2, 206),
            (3, 129),
            (10, 217),
            (10, 396),
            (6, 175),
            (7, 431),
            (1, 87),
            (10, 188),
            (7, 28),
            (4, 299),
            (9, 316),
            (8, 386),
            (4, 346),
            (4, 214),
            (5, 72),
            (4, 482),
            (5, 168),
            (6, 103),
            (4, 238),
            (10, 149),
            (5, 306),
            (3, 59),
            (2, 452),
            (6, 360),
            (1, 197),
            (3, 166),
            (6, 15),
            (1, 232),
            (7, 304),
            (5, 348),
            (9, 492),
            (4, 221),
            (3, 31),
            (9, 441),
            (2, 140),
            (5, 207),
            (8, 38),
            (10, 34),
            (7, 217),
            (8, 194),
            (1, 8),
            (6, 227),
            (8, 499),
            (10, 98),
            (10, 378),
            (9, 187),
            (2, 499),
            (1, 294),
            (6, 167),
            (7, 161),
            (1, 281),
            (5, 92),
            (9, 426),
            (9, 107),
            (3, 293),
            (9, 481),
            (4, 282),
            (2, 455),
            (4, 7),
            (10, 12),
            (8, 110),
            (6, 102),
            (2, 415),
            (9, 140),
            (3, 86),
            (5, 147),
            (1, 179),
            (4, 24),
            (3, 115),
            (2, 286),
            (2, 1),
            (5, 482),
            (5, 422),
            (3, 359),
            (5, 385),
            (5, 215),
            (8, 416),
            (3, 299),
            (9, 360),
            (4, 153),
            (7, 75),
            (3, 48),
            (9, 35),
            (2, 132),
            (9, 64),
            (10, 140),
            (8, 373),
            (2, 158),
            (4, 369),
            (10, 449),
            (7, 119),
            (1, 447),
            (4, 413),
            (10, 279),
            (3, 492),
            (1, 314),
            (5, 339),
            (4, 458),
            (3, 294),
            (1, 343),
            (4, 132),
            (5, 107),
            (7, 100),
            (4, 222),
            (2, 480),
            (10, 204),
            (5, 318),
            (8, 86),
            (1, 174),
            (7, 110),
            (5, 228),
            (3, 415),
            (9, 172),
            (8, 80),
            (6, 162),
            (10, 45),
            (10, 154),
            (7, 171),
            (6, 250),
            (7, 155),
            (8, 90),
            (2, 29),
            (4, 69),
            (3, 297),
            (9, 181),
            (7, 377),
            (6, 182),
            (9, 117),
            (7, 291),
            (9, 123),
            (5, 10),
            (7, 256),
            (6, 4),
            (3, 459),
            (3, 361),
            (2, 389),
            (6, 254),
            (8, 112),
            (7, 115),
            (5, 470),
            (1, 194),
            (2, 3),
            (5, 143),
            (8, 440),
            (4, 195),
            (10, 164),
            (5, 201),
            (9, 175),
            (7, 104),
            (1, 307),
            (1, 183),
            (3, 41),
            (4, 367),
            (10, 452),
            (7, 9),
            (1, 247),
            (10, 417),
            (9, 104),
            (10, 92),
            (10, 463),
            (6, 19),
            (9, 213),
            (9, 14),
            (8, 409),
            (2, 257),
            (7, 383),
            (5, 493),
            (1, 122),
            (4, 31),
            (8, 1),
            (9, 307),
            (10, 56),
            (4, 82),
            (5, 229),
            (5, 111),
            (10, 4),
            (8, 435),
            (10, 349),
            (3, 50),
            (9, 46),
            (6, 72),
            (1, 161),
            (7, 205),
            (10, 251),
            (5, 65),
            (8, 58),
            (3, 375),
            (3, 51),
            (6, 447),
            (6, 88),
            (1, 296),
            (5, 456),
            (9, 289),
            (8, 81),
            (1, 154),
            (1, 425),
            (9, 486),
            (9, 430),
            (2, 61),
            (4, 83),
            (10, 410),
            (6, 121),
            (3, 412),
            (3, 443),
            (5, 274),
            (7, 11),
            (5, 352),
            (2, 89),
            (9, 483),
            (2, 463),
            (8, 270),
            (3, 153),
            (5, 191),
            (3, 33),
            (7, 69),
            (9, 392),
            (5, 230),
            (2, 85),
            (4, 402),
            (7, 284),
            (4, 190),
            (5, 63),
            (4, 337),
            (1, 285),
            (3, 90),
            (4, 116),
            (8, 366),
            (3, 73),
            (6, 498),
            (1, 417),
            (10, 353),
            (3, 272),
            (6, 308),
            (4, 470),
            (4, 356),
            (7, 31),
            (1, 55),
            (8, 299),
            (2, 474),
            (7, 163),
            (10, 319),
            (2, 438),
            (6, 428),
            (5, 4),
            (4, 364),
            (5, 136),
            (1, 129),
            (4, 464),
            (2, 21),
            (7, 432),
            (9, 348),
            (5, 160),
            (7, 174),
            (6, 189),
            (1, 203),
            (5, 204),
            (8, 376),
            (1, 392),
            (9, 115),
            (3, 259),
            (8, 279),
            (3, 287),
            (6, 35),
            (4, 191),
            (2, 28),
            (4, 335),
            (7, 59),
            (8, 191),
            (1, 489),
            (9, 397),
            (9, 17),
            (8, 336),
            (3, 201),
            (7, 275),
            (9, 302),
            (4, 454),
            (6, 464),
            (4, 368),
            (9, 311),
            (1, 283),
            (10, 207),
            (7, 440),
            (9, 249),
            (7, 422),
            (7, 248),
            (6, 55),
            (2, 67),
            (3, 184),
            (5, 114),
            (3, 283),
            (8, 401),
            (4, 11),
            (2, 449),
            (9, 295),
            (4, 148),
            (6, 357),
            (8, 323),
            (1, 301),
            (3, 337),
            (6, 369),
            (3, 458),
            (5, 317),
            (4, 439),
            (1, 324),
            (7, 401),
            (4, 154),
            (6, 112),
            (10, 432),
            (9, 267),
            (3, 148),
            (3, 471),
            (3, 289),
            (3, 106),
            (1, 121),
            (1, 416),
            (10, 180),
            (8, 136),
            (9, 343),
            (2, 119),
            (3, 127),
            (9, 121),
            (4, 17),
            (10, 380),
            (10, 297),
            (7, 474),
            (5, 87),
            (8, 452),
            (4, 41),
            (9, 102),
            (10, 357),
            (3, 397),
            (3, 143),
            (3, 429),
            (2, 254),
            (7, 183),
            (4, 497),
            (4, 348),
            (10, 10),
            (9, 432),
            (9, 345),
            (6, 378),
            (10, 274),
            (5, 152),
            (6, 211),
            (3, 164),
            (5, 461),
            (10, 422),
            (10, 298),
            (7, 145),
            (6, 177),
            (6, 81),
            (4, 401),
            (1, 288),
            (10, 156),
            (6, 389),
            (2, 475),
            (3, 191),
            (6, 468),
            (10, 369),
            (9, 442),
            (4, 12),
            (7, 356),
            (5, 32),
            (8, 236),
            (6, 74),
            (7, 362),
            (6, 442),
            (4, 210),
            (5, 475),
            (1, 115),
            (6, 345),
            (4, 144),
            (1, 128),
            (6, 460),
            (7, 339),
            (4, 278),
            (6, 444),
            (1, 127),
            (8, 228),
            (9, 359),
            (5, 356),
            (9, 447),
            (5, 365),
            (10, 134),
            (8, 341),
            (7, 84),
            (1, 149),
            (2, 369),
            (3, 56),
            (10, 113),
            (3, 386),
            (2, 23),
            (9, 118),
            (9, 138),
            (6, 77),
            (9, 178),
            (10, 77),
            (8, 68),
            (1, 191),
            (5, 250),
            (8, 329),
            (3, 109),
            (8, 302),
            (4, 218),
            (3, 212),
            (6, 423),
            (5, 363),
            (8, 55),
            (3, 169),
            (8, 45),
            (8, 13),
            (10, 442),
            (6, 321),
            (7, 330),
            (10, 2),
            (4, 405),
            (7, 361),
            (5, 447),
            (3, 475),
            (6, 128),
            (2, 123),
            (3, 481),
            (5, 85),
            (6, 483),
            (4, 142),
            (2, 321),
            (5, 198),
            (7, 277),
            (2, 163),
            (2, 199),
            (2, 331),
            (1, 85),
            (7, 42),
            (4, 100),
            (4, 75),
            (7, 214),
            (8, 113),
            (6, 415),
            (7, 370),
            (10, 54),
            (1, 455),
            (6, 436),
            (5, 313),
            (6, 329),
            (3, 58),
            (1, 27),
            (1, 144),
            (4, 66),
            (8, 446),
            (8, 339),
            (8, 169),
            (9, 264),
            (7, 274),
            (9, 260),
            (10, 499),
            (10, 59),
            (3, 295),
            (3, 105),
            (8, 9),
            (5, 425),
            (8, 443),
            (5, 342),
            (10, 41),
            (5, 137),
            (10, 13),
            (3, 310),
            (3, 209),
            (2, 359),
            (6, 230),
            (4, 321),
            (5, 217),
            (4, 418),
            (4, 240),
            (5, 372),
            (7, 498),
            (9, 133),
            (6, 493),
            (8, 226),
            (6, 149),
            (10, 359),
            (1, 363),
            (4, 35),
            (2, 232),
            (5, 82),
            (3, 3),
            (6, 445),
            (8, 397),
            (6, 455),
            (4, 477),
            (9, 26),
            (10, 441),
            (1, 165),
            (3, 302),
            (7, 489),
            (7, 13),
            (3, 142),
            (9, 30),
            (7, 380),
            (7, 21),
            (7, 225),
            (7, 469),
            (8, 388),
            (7, 149),
            (9, 11),
            (6, 350),
            (5, 68),
            (4, 494),
            (7, 90),
            (10, 419),
            (3, 372),
            (2, 88),
            (1, 454),
            (9, 324),
            (1, 406),
            (6, 34),
            (4, 95),
            (8, 439),
            (8, 403),
            (3, 15),
            (4, 329),
            (2, 215),
            (2, 386),
            (7, 173),
            (6, 114),
            (7, 301),
            (4, 294),
            (1, 310),
            (2, 19),
            (3, 319),
            (10, 158),
            (7, 218),
            (7, 27),
            (4, 107),
            (5, 95),
            (7, 257),
            (10, 265),
            (4, 254),
            (2, 72),
            (8, 277),
            (4, 267),
            (3, 409),
            (4, 355),
            (5, 141),
            (2, 373),
            (4, 322),
            (4, 137),
            (3, 379),
            (4, 53),
            (1, 463),
            (10, 14),
            (5, 69),
            (1, 394),
            (10, 269),
            (4, 437),
            (3, 116),
            (4, 5),
            (6, 201),
            (2, 298),
            (2, 52),
            (3, 393),
            (9, 110),
            (10, 96),
            (10, 347),
            (2, 292),
            (7, 385),
            (7, 372),
            (7, 114),
            (2, 364),
            (2, 459),
            (4, 232),
            (8, 454),
            (10, 91),
            (5, 238),
            (1, 257),
            (6, 286),
            (4, 9),
            (10, 186),
            (9, 166),
            (5, 269),
            (3, 81),
            (9, 112),
            (5, 332),
            (4, 445),
            (4, 342),
            (4, 48),
            (4, 379),
            (7, 331),
            (2, 76),
            (7, 121),
            (4, 181),
            (2, 159),
            (2, 311),
            (1, 53),
            (6, 374),
            (3, 326),
            (10, 273),
            (3, 231),
            (10, 282),
            (7, 302),
            (2, 150),
            (4, 157),
            (2, 144),
            (10, 206),
            (1, 229),
            (9, 275),
            (9, 259),
            (10, 287),
            (5, 154),
            (5, 208),
            (8, 480),
            (5, 483),
            (6, 165),
            (6, 169),
            (8, 359),
            (8, 383),
            (5, 181),
            (10, 148),
            (2, 192),
            (10, 341),
            (3, 284),
            (1, 403),
            (9, 309),
            (10, 177),
            (4, 380),
            (3, 91),
            (4, 331),
            (10, 266),
            (10, 256),
            (2, 351),
            (8, 4),
            (7, 8),
            (5, 79),
            (3, 78),
            (8, 147),
            (10, 111),
            (4, 18),
            (8, 340),
            (10, 340),
            (5, 471),
            (9, 425),
            (2, 205),
            (7, 357),
            (3, 234),
            (6, 306),
            (7, 147),
            (4, 390),
            (5, 139),
            (5, 135),
            (3, 488),
            (9, 206),
            (4, 496),
            (7, 235),
            (6, 27),
            (1, 365),
            (9, 263),
            (2, 225),
            (3, 141),
            (2, 291),
            (9, 488),
            (2, 31),
            (6, 23),
            (10, 440),
            (8, 235),
            (4, 432),
            (6, 296),
            (9, 203),
            (9, 144),
            (9, 212),
            (3, 76),
            (6, 213),
            (9, 243),
            (8, 465),
            (9, 278),
            (2, 203),
            (6, 424),
            (1, 420),
            (3, 158),
            (1, 133),
            (9, 137),
            (9, 142),
            (10, 338),
            (7, 485),
            (7, 407),
            (3, 358),
            (4, 129),
            (8, 30),
            (7, 52),
            (5, 357),
            (5, 285),
            (2, 104),
            (5, 218),
            (4, 81),
            (4, 284),
            (5, 459),
            (5, 20),
            (4, 192),
            (9, 37),
            (6, 410),
            (10, 20),
            (8, 100),
            (2, 457),
            (4, 188),
            (8, 179),
            (3, 277),
            (10, 90),
            (8, 142),
            (1, 214),
            (10, 360),
            (10, 234),
            (1, 498),
            (10, 367),
            (8, 73),
            (2, 249),
            (2, 268),
            (8, 150),
            (6, 398),
            (6, 472),
            (8, 202),
            (4, 476),
            (4, 403),
            (5, 159),
            (3, 427),
            (10, 408),
            (6, 96),
            (7, 160),
            (7, 303),
            (6, 48),
            (4, 377),
            (4, 256),
            (6, 14),
            (4, 64),
            (7, 378),
            (10, 374),
            (9, 192),
            (8, 26),
            (3, 159),
            (1, 219),
            (5, 35),
            (4, 358),
            (10, 63),
            (5, 43),
            (6, 132),
            (5, 77),
            (10, 370),
            (3, 270),
            (10, 8),
            (9, 477),
            (3, 121),
            (5, 343),
            (3, 65),
            (9, 103),
            (10, 262),
            (1, 182),
            (4, 173),
            (10, 225),
            (2, 383),
            (7, 373),
            (1, 325),
            (2, 265),
            (7, 405),
            (3, 210),
            (5, 138),
            (8, 338),
            (8, 42),
            (5, 195),
            (7, 143),
            (5, 49),
            (6, 404),
            (2, 270),
            (6, 290),
            (2, 105),
            (8, 105),
            (10, 23),
            (2, 428),
            (9, 162),
            (8, 381),
            (7, 324),
            (8, 6),
            (7, 126),
            (4, 350),
            (9, 460),
            (3, 9),
            (2, 434),
            (3, 133),
            (1, 348),
            (5, 1),
            (9, 312),
            (6, 220),
            (6, 90),
            (4, 20),
            (2, 56),
            (3, 199),
            (7, 66),
            (9, 420),
            (2, 124),
            (7, 338),
            (9, 320),
            (10, 30),
            (4, 303),
            (6, 393),
            (4, 133),
            (2, 64),
            (10, 468),
            (3, 368),
            (1, 449),
            (7, 364),
            (1, 275),
            (4, 101),
            (9, 97),
            (8, 3),
            (8, 464),
            (7, 258),
            (4, 122),
            (10, 28),
            (1, 412),
            (9, 74),
            (1, 97),
            (4, 179),
            (1, 38),
            (2, 496),
            (9, 56),
            (2, 405),
            (4, 313),
            (2, 219),
            (3, 126),
            (5, 101),
            (7, 345),
            (3, 220),
            (3, 226),
            (4, 21),
            (8, 489),
            (5, 329),
            (10, 371),
            (10, 173),
            (8, 155),
            (3, 134),
            (10, 191),
            (3, 420),
            (10, 255),
            (2, 110),
            (2, 489),
            (5, 354),
            (6, 441),
            (7, 86),
            (8, 396),
            (3, 232),
            (3, 292),
            (7, 437),
            (2, 20),
            (7, 261),
            (2, 258),
            (5, 255),
            (9, 222),
            (5, 464),
            (5, 172),
            (7, 336),
            (2, 367),
            (4, 423),
            (5, 455),
            (10, 152),
            (9, 164),
            (1, 490),
            (6, 305),
            (1, 86),
            (8, 149),
            (9, 85),
            (1, 446),
            (10, 248),
            (8, 370),
            (9, 437),
            (5, 236),
            (6, 333),
            (1, 496),
            (8, 455),
            (8, 238),
            (3, 495),
            (6, 13),
            (7, 264),
            (3, 130),
            (9, 469),
            (5, 210),
            (5, 375),
            (5, 226),
            (8, 419),
            (9, 271),
            (4, 279),
            (5, 100),
            (2, 8),
            (10, 123),
            (3, 243),
            (1, 476),
            (8, 29),
            (9, 80),
            (8, 488),
            (5, 45),
            (2, 17),
            (5, 133),
            (3, 463),
            (4, 444),
            (9, 498),
            (6, 139),
            (4, 44),
            (1, 374),
            (10, 136),
            (8, 166),
            (8, 394),
            (10, 488),
            (9, 335),
            (10, 94),
            (9, 208),
            (5, 265),
            (1, 284),
            (3, 352),
            (8, 474),
            (8, 317),
            (10, 81),
            (7, 99),
            (2, 136),
            (5, 134),
            (6, 368),
            (9, 83),
            (6, 463),
            (4, 462),
            (2, 426),
            (3, 206),
            (4, 436),
            (4, 216),
            (1, 3),
            (7, 326),
            (9, 47),
            (2, 130),
            (4, 394),
            (10, 142),
            (3, 163),
            (6, 343),
            (7, 342),
            (6, 373),
            (3, 136),
            (6, 440),
            (8, 415),
            (10, 300),
            (3, 30),
            (8, 16),
            (2, 285),
            (10, 147),
            (2, 122),
            (7, 416),
            (8, 262),
            (4, 499),
            (9, 299),
            (6, 267),
            (1, 19),
            (7, 111),
            (10, 487),
            (10, 223),
            (7, 142),
            (1, 259),
            (2, 75),
            (7, 208),
            (4, 291),
            (3, 87),
            (6, 58),
            (9, 353),
            (10, 373),
            (6, 446),
            (4, 371),
            (6, 194),
            (8, 10),
            (7, 393),
            (6, 229),
            (7, 169),
            (5, 233),
            (6, 10),
            (9, 224),
            (1, 44),
            (2, 148),
            (5, 448),
            (3, 343),
            (8, 267),
            (2, 485),
            (7, 135),
            (4, 162),
            (8, 205),
            (1, 68),
            (9, 328),
            (7, 2),
            (2, 272),
            (4, 385),
            (2, 473),
            (1, 24),
            (2, 339),
            (3, 176),
            (9, 479),
            (9, 98),
            (4, 242),
            (7, 137),
            (4, 46),
            (5, 223),
            (2, 407),
            (7, 20),
            (6, 170),
            (9, 250),
            (7, 263),
            (8, 451),
            (7, 479),
            (8, 294),
            (3, 438),
            (2, 216),
            (8, 431),
            (10, 215),
            (1, 66),
            (6, 358),
            (10, 320),
            (1, 327),
            (10, 214),
            (2, 300),
            (6, 73),
            (7, 328),
            (8, 106),
            (3, 387),
            (4, 456),
            (1, 108),
            (7, 294),
            (10, 444),
            (7, 412),
            (3, 374),
            (10, 76),
            (1, 452),
            (6, 457),
            (5, 62),
            (4, 146),
            (7, 329),
            (3, 474),
            (2, 429),
            (9, 421),
            (9, 338),
            (6, 17),
            (1, 291),
            (2, 229),
            (7, 445),
            (4, 79),
            (8, 300),
            (7, 425),
            (9, 1),
            (2, 376),
            (7, 200),
            (5, 173),
            (10, 306),
            (10, 345),
            (1, 385),
            (7, 374),
            (5, 281),
            (8, 412),
            (2, 95),
            (10, 93),
            (2, 194),
            (9, 242),
            (9, 456),
            (4, 108),
            (7, 207),
            (5, 16),
            (6, 63),
            (10, 364),
            (9, 342),
            (4, 452),
            (6, 334),
            (1, 408),
            (8, 47),
            (4, 485),
            (2, 324),
            (1, 95),
            (1, 109),
            (3, 306),
            (1, 32),
            (6, 406),
            (8, 487),
            (2, 377),
            (8, 254),
            (8, 210),
            (6, 261),
            (6, 370),
            (1, 1),
            (5, 219),
            (3, 237),
            (8, 246),
            (10, 60),
            (10, 416),
            (2, 481),
            (9, 95),
            (6, 252),
            (7, 136),
            (5, 124),
            (6, 76),
            (4, 23),
            (6, 452),
            (3, 135),
            (10, 491),
            (9, 152),
            (3, 182),
            (1, 225),
            (2, 263),
            (3, 68),
            (5, 322),
            (10, 175),
            (6, 485),
            (2, 493),
            (2, 151),
            (10, 462),
            (1, 162),
            (9, 229),
            (5, 393),
            (1, 262),
            (8, 48),
            (10, 333),
            (2, 269),
            (3, 496),
            (9, 180),
            (10, 131),
            (4, 316),
            (1, 204);
            ''')


def downgrade():
    op.execute('DELETE FROM user_genre WHERE 1=1')
