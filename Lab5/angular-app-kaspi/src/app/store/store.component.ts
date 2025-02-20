import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductListComponent } from '../product-list/product-list.component';

interface Product {
  name: string;
  description: string;
  rating: number;
  likes: number;
  image: string;
  link: string;
}

@Component({
  selector: 'app-store',
  standalone: true,
  imports: [CommonModule, ProductListComponent],
  templateUrl: './store.component.html',
  styleUrl: './store.component.css'
})
export class StoreComponent {
  categories = ['Ноутбуки', 'Компьютерные мыши', 'Компьютерные коврики', 'Клавиатуры'];
  selectedCategory = 'Products';

  likedProducts = new Set<string>();

  products: Record<string, Product[]> = {
    'Компьютерные мыши':[
    {
      image:'https://resources.cdn-kaspi.kz/img/m/p/hb2/hc2/64119540187166.jpg?format=preview-large',
      name:'Logitech G102 Lightsync черный',
      description:'Мышь проводная Logitech G102 LightSync позволяет играть с максимальной эффективностью. В мышке применяется датчик игрового уровня с чувствительностью 8000 dpi, регулируемой в широком диапазоне отдельной кнопкой. ',
      rating:5,
      link:'https://kaspi.kz/shop/p/logitech-g102-lightsync-chernyi-100956618/?c=750000000',
      likes: 0
    },
  ],
    'Клавиатуры':[
    {
      image:'https://resources.cdn-kaspi.kz/img/m/p/pdc/p8a/24789850.jpg?format=preview-large',
      name:'AULA F75 белый',
      description:'Aula f75 - это лучшая бюджетная клавиатура. Если Ваш выбор - цена/качество, тогда это идеальный вариант. ',
      rating:5,
      link:'https://kaspi.kz/shop/p/aula-f75-belyi-117731409/?c=750000000',
      likes: 0
    },
  ],
    'Компьютерные коврики':[
    {
      image:'https://resources.cdn-kaspi.kz/img/m/p/he5/h4a/84701020356638.jpg?format=preview-large',
      name:'Inova Death Life',
      description:'Это удобный аксессуар, который обеспечивает плавное и точное движение мыши. Поверхность разработана для комфортной работы, поддерживая как оптические, так и лазерные мыши.',
      rating:5,
      link:'https://kaspi.kz/shop/p/inova-death-life-115283473/?c=750000000',
      likes: 0
    },
  ],
    'Ноутбуки':[
    {
      image:'https://resources.cdn-kaspi.kz/img/m/p/h89/haa/64373052571678.jpg?format=preview-large',
      name:'Lenovo IdeaPad 3 15.6" / 4 Гб / SSD 256 Гб / Без ОС / 15IGL05 /',
      description:'IdeaPad 3 стоит, как обычный ноутбук для повседневного использования, однако это устройство способно на большее. Модель, оснащенная процессором Intel Celeron, оперативной памятью объемом 4 ГБ и SSD накопителем, превзойдет любые ваши ожидания. ',
      rating:4,
      link:'https://kaspi.kz/shop/p/lenovo-ideapad-3-15-6-4-gb-ssd-256-gb-bez-os-15igl05-81wq00emrk-102878742/?c=750000000',
      likes: 2
    },
    {
      image:'https://resources.cdn-kaspi.kz/img/m/p/h0d/hc8/84558388887582.jpg?format=preview-large',
      name:'Acer Aspire 3 15.6" / 8 Гб / SSD 256 Гб / Win 11 / A315-35 /',
      description:'Воспроизводите видео быстро и без задержек, просматривайте веб-страницы или выполняйте рабочие задачи благодаря процессору и видеокарте от Intel®. ',
      rating:4,
      link:'https://kaspi.kz/shop/p/acer-aspire-3-15-6-8-gb-ssd-256-gb-win-11-a315-35-nx-a9aex-00h-114792265/?c=750000000',
      likes: 6
    },
    {
      image:'https://resources.cdn-kaspi.kz/img/m/p/p59/p53/15221547.jpg?format=preview-large',
      name:'Lenovo LOQ 15.6" / 16 Гб / SSD 512 Гб / Без ОС / 15IAX9 /',
      description:'Ноутбук хороший. Качество отличное. Игры тянет нормально, но экран маловат, лучше купить монитор. ',
      rating:4,
      link:'https://kaspi.kz/shop/p/lenovo-loq-15-6-16-gb-ssd-512-gb-bez-os-15iax9-83gs005nrk-120581412/?c=750000000',
      likes: 3
    },
    {
      image:'https://resources.cdn-kaspi.kz/img/m/p/hd3/h97/85277334405150.jpg?format=preview-large',
      name:'ThundeRobot 911 X Wild Hunter G2L 15.6" / 16 Гб / SSD 512 Гб /',
      description:'Игровой ноутбук THUNDEROBOT 911 X Wild Hunter G2L получил мощные компоненты, которые скрыты в тонком металлическом корпусе. ',
      rating:5,
      link:'https://kaspi.kz/shop/p/thunderobot-911-x-wild-hunter-g2l-15-6-16-gb-ssd-512-gb-win-11-pro-jt009500e-116983567/?c=750000000',
      likes: 2
    },
    {
      image:'https://resources.cdn-kaspi.kz/img/m/p/p27/pb4/9286973.jpeg?format=preview-large',
      name:'HYDRA H20 15.6" / 12 Гб / SSD 512 Гб / Win 11 / MKII',
      description:'HYDRA H20 стоит, как обычный ноутбук для повседневного использования, однако это устройство достаточно мощное. ',
      rating:5,
      link:'https://kaspi.kz/shop/p/hydra-h20-15-6-12-gb-ssd-512-gb-win-11-mkii-115019992/?c=750000000',
      likes: 1
    },
    {
      image:'https://resources.cdn-kaspi.kz/img/m/p/p79/p58/7357175.jpg?format=preview-large',
      name:'Acer Aspire Lite 15.6" / 8 Гб / SSD 256 Гб / Win 11 Pro / AL15-31P /',
      description:'Отличные, работает хорошо, офис и ПО установлены, что очень упрощает жизнь и время.',
      rating:4,
      link:'https://kaspi.kz/shop/p/acer-aspire-lite-15-6-8-gb-ssd-256-gb-win-11-pro-al15-31p-nx-kz7er-01w-129758983/?c=750000000',
      likes: 1
    },
    {
      image:'https://resources.cdn-kaspi.kz/img/m/p/hf4/h52/64509322919966.jpg?format=preview-large',
      name:'Apple MacBook Air 13 2022 13.6" / 8 Гб / SSD 256 Гб / macOS /',
      description:'MacBook Air 2022 года можно назвать одним из крупнейших обновлений линейки за всю историю. Он полностью изменился внешне, получил более новый и мощный процессор M2. ',
      rating:4,
      link:'https://kaspi.kz/shop/p/apple-macbook-air-13-2022-13-6-8-gb-ssd-256-gb-macos-mlxw3-105933794/?c=750000000',
      likes: 5
    },
  ]
  };

  get currentProducts(): Product[]{
    return this.products[this.selectedCategory] || [];
  }

  selectCategory(category: string){
    this.selectedCategory = category;
  }

  likeProduct(productName: string){
    const product = this.products[this.selectedCategory].find(p => p.name === productName);
    if(!product) return;

    if(this.likedProducts.has(productName)){
      product.likes--;
      this.likedProducts.delete(productName);
    } else {
      product.likes++;
      this.likedProducts.add(productName);
    }
  }

  removeProduct(index: number){
    this.products[this.selectedCategory].splice(index, 1)
  }

  share(link: string){
    const msg = encodeURIComponent(`Check it out: ${link}`);
    window.open(`https://t.me/share/url?url=${link}&text${msg}`, '_blank');
  }
}
