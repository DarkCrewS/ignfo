a
    ܶv`  ?                   @   s,   d dl Zd dlZd dlZd dlT dd? ZdS )?    N)?*c                 C   s?   d}t ?|| ?}|d kr"td? ntd? | ?d?}t|d ?}tj?|d?}|d j}t|?}td|?	? ? d	}t
?? }|?d? |?|? |?|j? |?|? |?t| ??\}	}
|??  |	d
kr?td? ntd? d S )NzD^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$zregex : failzregex : success?@?   ZMXr   zmx :zno-reply@gmail.com??   zsmtp : successzsmtp : fail)?r?match?print?split?str?dnsZresolverZresolveZexchange?lower?smtplibZSMTPZset_debuglevel?connectZheloZlocal_hostname?mailZrcpt?quit)r   Zregexr   ZsplitAddressZdomainZrecordsZmxrZfromaddrr   ?code?message? r   ?check_mail.py?validate_mail   s,    






r   )?rer   r   Zdns.resolverr   Zlocalr   r   r   r   r   ?<module>   s   