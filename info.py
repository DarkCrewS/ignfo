a
    �w�`-  �                   @   s~   d dl Z d dlZej�e �� d � d dlZd dlT e�� Zej	ddddd� e
e�� �Ze �d	� ed
 rzeed
 d� dS )�    Nz/.lib/)�*z-uz--userTzusername of account to scan)Zrequired�help�cls�user)Zusrname)�os�sys�path�append�getcwd�argparseZapi�ArgumentParserZap�add_argument�vars�
parse_args�args�systemZ	user_info� r   r   �info.py�<module>   s   
