import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Album {
  id: number;
  title: string;
}

export interface Photo {
  id: number;
  albumId: number;
  title: string;
  url: string;
}

@Injectable({
  providedIn: 'root'
})

export class AlbumsService {

  private baseUrl = "https://jsonplaceholder.typicode.com";

  constructor(private http: HttpClient) {}

  // album-detail component
  getAlbums(): Observable<Album[]>{
    return this.http.get<Album[]>(`${this.baseUrl}/albums`);
  }

  getAlbum(id: number): Observable<Album>{
    return this.http.get<Album>(`${this.baseUrl}/albums/${id}`)
  }

  deleteAlbum(id: number): Observable<any>{
    return this.http.delete(`${this.baseUrl}/albums/${id}`);
  }

  updateAlbum(id: number, title: string): Observable<Album>{
    return this.http.put<Album>(`${this.baseUrl}/albums/${id}`, {title});
  }

  getPhotos(albumId: number): Observable<Photo[]>{
    return this.http.get<Photo[]>(`${this.baseUrl}/albums/${albumId}/photos`);
  }
}
